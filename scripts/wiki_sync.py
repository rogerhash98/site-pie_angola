#!/usr/bin/env python3
"""
wiki_sync.py — Gera documentação Markdown do projecto Django PIE Angola
e escreve directamente nas gavetas semânticas de um Vault Obsidian.

Stack: Python 3.10+ stdlib only. Sem dependências externas.

Fluxo:
    1. Varre o projecto aplicando o filtro de ruído.
    2. Classifica cada ficheiro numa gaveta semântica do Vault.
    3. Gera notas .md com frontmatter + conteúdo + wikilinks.
    4. Escreve cada nota directamente na subpasta correcta do Vault.
    5. Cria um MOC (Map of Content) na raiz e índices por gaveta.

Wikilinks: as notas usam nomes únicos prefixados (ex: [[view-home]],
[[tpl-about]]). O Obsidian resolve wikilinks por nome em todo o Vault,
portanto reorganizar pastas não quebra ligações.

Uso:
    python scripts/wiki_sync.py                          # usa defaults
    OBSIDIAN_VAULT=/caminho/vault python scripts/wiki_sync.py
    python scripts/wiki_sync.py --vault /caminho/vault --dry-run
    python scripts/wiki_sync.py --vault /caminho/vault --clean
"""
from __future__ import annotations

import argparse
import ast
import hashlib
import os
import re
import shutil
import sys
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path

# ---------------------------------------------------------------------------
# CONFIGURAÇÃO
# ---------------------------------------------------------------------------

PROJECT_ROOT = Path(__file__).resolve().parent.parent
PROJECT_NAME = "PIE Angola"

# Vault por defeito: pasta `doc/` dentro do próprio projecto.
# Cada projecto tem o seu Vault local — centro de memória versionável.
DEFAULT_VAULT = PROJECT_ROOT / "doc"

# Gavetas semânticas (alinhadas com as instruções do projecto:
# doc/visao/, doc/arquitectura/, doc/erros/, doc/decisoes/, doc/sessoes/, ...)
DRAWERS: dict[str, str] = {
    "visao":         "Visão geral do projecto e MOC raiz",
    "arquitectura":  "Configuração Django, settings, ASGI/WSGI, estrutura",
    "rotas":         "URLconf — mapeamento URL → view",
    "views":         "Funções de view Django",
    "templates":     "Páginas HTML (templates de topo)",
    "componentes":   "Componentes reutilizáveis (footer, menu, help_chat)",
    "produtos":      "Páginas de produto (winrest_nx, pingwin_bo)",
    "assets":        "Inventário de assets estáticos (CSS/JS/imagens)",
    "stack":         "Stack técnica, dependências e versões",
    "sessoes":       "Log manual de sessões de trabalho",
    "erros":         "Registo de erros encontrados e resoluções",
    "decisoes":      "ADRs — decisões técnicas",
}

# Filtro de ruído — pastas e ficheiros a ignorar por completo
IGNORE_DIRS: set[str] = {
    "__pycache__", ".git", ".venv", "venv", "env", "node_modules",
    ".idea", ".vscode", ".pytest_cache", ".mypy_cache", ".ruff_cache",
    "migrations", "staticfiles", "media", "dist", "build", ".tox",
    "scripts",  # o próprio script não se documenta
    "doc",      # o Vault local não se documenta a si mesmo
}

IGNORE_FILES: set[str] = {
    "db.sqlite3", "uv.lock", "poetry.lock", "package-lock.json",
    "yarn.lock", ".DS_Store", ".env", ".env.local", ".gitignore",
    "asgi.py", "wsgi.py", "manage.py",  # boilerplate Django
}

# Extensões binárias / não-textuais — só entram no inventário de Assets
BINARY_EXT: set[str] = {
    ".png", ".jpg", ".jpeg", ".gif", ".svg", ".ico", ".webp",
    ".woff", ".woff2", ".ttf", ".otf", ".eot",
    ".mp4", ".mp3", ".pdf", ".zip", ".gz",
}

# Limite de tamanho (KB) para incluir conteúdo bruto na nota
MAX_INLINE_KB = 80


# ---------------------------------------------------------------------------
# MODELO
# ---------------------------------------------------------------------------

@dataclass
class Note:
    """Representa uma nota Markdown a escrever no Vault."""
    drawer: str               # ex: "03-Views"
    slug: str                 # nome único: "view-home"
    title: str                # título humano: "View · home"
    source: Path | None       # ficheiro de origem (para frontmatter)
    body: str                 # corpo Markdown
    tags: list[str] = field(default_factory=list)
    links: list[str] = field(default_factory=list)  # wikilinks relacionados

    def render(self) -> str:
        """Devolve a nota completa com frontmatter YAML."""
        rel = self.source.relative_to(PROJECT_ROOT).as_posix() if self.source else ""
        fm = [
            "---",
            f"title: {self.title}",
            f"drawer: {self.drawer}",
            f"source: {rel}" if rel else "source: (gerado)",
            f"updated: {datetime.now().isoformat(timespec='seconds')}",
            f"tags: [{', '.join(self.tags)}]" if self.tags else "tags: []",
            "---",
            "",
        ]
        out = "\n".join(fm) + self.body.rstrip() + "\n"
        if self.links:
            out += "\n## Relacionados\n"
            out += "\n".join(f"- [[{lk}]]" for lk in self.links) + "\n"
        return out


# ---------------------------------------------------------------------------
# UTILS
# ---------------------------------------------------------------------------

def slugify(value: str) -> str:
    """Slug seguro para nome de ficheiro Obsidian."""
    value = re.sub(r"[^\w\-]+", "-", value.lower()).strip("-")
    return re.sub(r"-+", "-", value) or "untitled"


def is_ignored(path: Path) -> bool:
    """True se o caminho cair no filtro de ruído."""
    parts = set(path.parts)
    if parts & IGNORE_DIRS:
        return True
    if path.name in IGNORE_FILES:
        return True
    if path.suffix in BINARY_EXT:
        return False  # binários entram só no inventário de assets
    # __init__.py vazios não trazem valor
    if path.name == "__init__.py" and path.exists() and path.stat().st_size == 0:
        return True
    return False


def read_text(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except (UnicodeDecodeError, OSError):
        return ""


def fence(content: str, lang: str = "") -> str:
    """Bloco de código Markdown."""
    return f"```{lang}\n{content.rstrip()}\n```\n"


# ---------------------------------------------------------------------------
# GERADORES POR TIPO
# ---------------------------------------------------------------------------

def gen_visao() -> Note:
    """Nota raiz com README + visão do projecto."""
    readme = PROJECT_ROOT / "README.md"
    body = [f"# {PROJECT_NAME}\n",
            "Site institucional Django para PIE Angola.\n",
            "## Conteúdo do README\n"]
    body.append(fence(read_text(readme) or "(README vazio)", "markdown"))
    body.append("## Pontos de entrada\n")
    body.append("- [[arq-settings]] — configuração Django")
    body.append("- [[rotas-urlconf]] — mapeamento de URLs")
    body.append("- [[stack-pyproject]] — dependências e versões\n")
    return Note(
        drawer="visao",
        slug="moc-pieangola",
        title=f"MOC · {PROJECT_NAME}",
        source=readme if readme.exists() else None,
        body="\n".join(body),
        tags=["moc", "visao"],
        links=["arq-settings", "rotas-urlconf", "stack-pyproject"],
    )


def gen_settings() -> Note | None:
    src = PROJECT_ROOT / "app" / "settings.py"
    if not src.exists():
        return None
    content = read_text(src)
    body = ["# Configuração Django\n",
            f"Ficheiro: `{src.relative_to(PROJECT_ROOT)}`\n",
            "## Conteúdo\n",
            fence(content, "python")]
    return Note(
        drawer="arquitectura",
        slug="arq-settings",
        title="Arquitectura · settings.py",
        source=src,
        body="\n".join(body),
        tags=["django", "config"],
    )


def gen_urls() -> tuple[Note, list[Note]]:
    """Gera nota índice de URLs + nota por rota."""
    src = PROJECT_ROOT / "app" / "urls.py"
    content = read_text(src)
    # Ignora exemplos do docstring: corta tudo antes de `urlpatterns`
    scan = content.split("urlpatterns =", 1)[-1]
    pat = re.compile(r"path\(\s*['\"]([^'\"]*)['\"]\s*,\s*([\w_.]+)\s*(?:,\s*name\s*=\s*['\"]([^'\"]+)['\"])?")
    rotas = pat.findall(scan)

    # Nota índice
    rows = ["| URL | View | Nome | Nota |", "|---|---|---|---|"]
    sub_notes: list[Note] = []
    for url, view, name in rotas:
        nslug = f"rota-{slugify(name or view)}"
        rows.append(f"| `/{url}` | `{view}` | `{name}` | [[{nslug}]] |")
        body = [
            f"# Rota · {name or view}\n",
            f"- **URL:** `/{url}`",
            f"- **View:** [[view-{slugify(view)}]]",
            f"- **Nome:** `{name}`\n",
            "## Definição\n",
            fence(f"path('{url}', {view}, name='{name}')", "python"),
        ]
        sub_notes.append(Note(
            drawer="rotas",
            slug=nslug,
            title=f"Rota · {name or view}",
            source=src,
            body="\n".join(body),
            tags=["rota", "url"],
            links=[f"view-{slugify(view)}"],
        ))

    index_body = ["# URLconf\n",
                  f"Ficheiro: `{src.relative_to(PROJECT_ROOT)}`\n",
                  "## Mapa de rotas\n",
                  "\n".join(rows), "",
                  "## Código completo\n",
                  fence(content, "python")]
    index = Note(
        drawer="rotas",
        slug="rotas-urlconf",
        title="Rotas · URLconf",
        source=src,
        body="\n".join(index_body),
        tags=["rotas", "django"],
        links=[n.slug for n in sub_notes],
    )
    return index, sub_notes


def gen_views() -> tuple[Note, list[Note]]:
    """Gera índice + nota por função de view (parsing AST)."""
    src = PROJECT_ROOT / "app" / "views.py"
    content = read_text(src)
    tree = ast.parse(content)

    notes: list[Note] = []
    for node in tree.body:
        if isinstance(node, ast.FunctionDef):
            snippet = ast.get_source_segment(content, node) or ""
            doc = ast.get_docstring(node) or "_(sem docstring)_"
            body = [
                f"# View · {node.name}\n",
                f"Função `{node.name}` definida em `{src.relative_to(PROJECT_ROOT)}`.\n",
                f"## Descrição\n{doc}\n",
                "## Código\n",
                fence(snippet, "python"),
            ]
            notes.append(Note(
                drawer="views",
                slug=f"view-{slugify(node.name)}",
                title=f"View · {node.name}",
                source=src,
                body="\n".join(body),
                tags=["view", "django"],
            ))

    index_body = ["# Views\n",
                  f"Total: **{len(notes)}** funções em `{src.relative_to(PROJECT_ROOT)}`.\n",
                  "## Lista\n",
                  "\n".join(f"- [[{n.slug}]]" for n in notes)]
    index = Note(
        drawer="views",
        slug="views-indice",
        title="Views · Índice",
        source=src,
        body="\n".join(index_body),
        tags=["views"],
        links=[n.slug for n in notes],
    )
    return index, notes


def gen_template_note(path: Path, drawer: str, prefix: str) -> Note:
    """Gera nota para um template HTML."""
    name = path.stem
    content = read_text(path)
    rel = path.relative_to(PROJECT_ROOT)

    # Detecta extends/include para criar wikilinks
    related: list[str] = []
    for m in re.finditer(r"{%\s*(extends|include)\s+['\"]([^'\"]+)['\"]", content):
        ref = Path(m.group(2)).stem
        related.append(f"tpl-{slugify(ref)}")

    size_kb = len(content.encode("utf-8")) / 1024
    body = [f"# Template · {name}\n",
            f"Ficheiro: `{rel}` ({size_kb:.1f} KB)\n"]
    if related:
        body.append("## Dependências de template\n")
        body.append("\n".join(f"- [[{r}]]" for r in related) + "\n")
    body.append("## Conteúdo\n")
    if size_kb <= MAX_INLINE_KB:
        body.append(fence(content, "html"))
    else:
        body.append(f"_(omitido — {size_kb:.1f} KB excede {MAX_INLINE_KB} KB)_\n")

    return Note(
        drawer=drawer,
        slug=f"{prefix}-{slugify(name)}",
        title=f"Template · {name}",
        source=path,
        body="\n".join(body),
        tags=["template", "html"],
        links=related,
    )


def gen_templates() -> list[Note]:
    """Classifica templates: páginas, componentes, produtos."""
    notes: list[Note] = []
    tpl_root = PROJECT_ROOT / "templates"
    if not tpl_root.exists():
        return notes

    for path in sorted(tpl_root.rglob("*.html")):
        if is_ignored(path):
            continue
        rel = path.relative_to(tpl_root)
        if rel.parts[0] == "components":
            notes.append(gen_template_note(path, "componentes", "cmp"))
        elif rel.parts[0] == "products":
            notes.append(gen_template_note(path, "produtos", "prod"))
        else:
            notes.append(gen_template_note(path, "templates", "tpl"))
    return notes


def gen_assets() -> Note:
    """Inventário de assets estáticos (sem conteúdo binário)."""
    static_root = PROJECT_ROOT / "static"
    rows = ["| Ficheiro | Tipo | Tamanho |", "|---|---|---|"]
    count = 0
    if static_root.exists():
        for p in sorted(static_root.rglob("*")):
            if p.is_file() and not is_ignored(p):
                rel = p.relative_to(PROJECT_ROOT)
                size = p.stat().st_size
                rows.append(f"| `{rel}` | {p.suffix or '?'} | {size} B |")
                count += 1
    body = ["# Inventário de Assets\n",
            f"Total: **{count}** ficheiros em `static/`.\n",
            "\n".join(rows)]
    return Note(
        drawer="assets",
        slug="assets-inventario",
        title="Assets · Inventário",
        source=static_root if static_root.exists() else None,
        body="\n".join(body),
        tags=["assets", "static"],
    )


def gen_stack() -> Note:
    src = PROJECT_ROOT / "pyproject.toml"
    content = read_text(src) if src.exists() else "(sem pyproject.toml)"
    body = ["# Stack técnica\n",
            f"Ficheiro: `{src.relative_to(PROJECT_ROOT) if src.exists() else 'n/a'}`\n",
            f"- **Python:** {sys.version.split()[0]}",
            "- **Framework:** Django",
            "- **Base de dados:** SQLite (dev)",
            "- **Templates:** Django Templates (HTML puro)\n",
            "## pyproject.toml\n",
            fence(content, "toml")]
    return Note(
        drawer="stack",
        slug="stack-pyproject",
        title="Stack · pyproject",
        source=src if src.exists() else None,
        body="\n".join(body),
        tags=["stack", "deps"],
    )


def gen_placeholder(drawer: str, slug: str, title: str, intro: str) -> Note:
    body = [f"# {title}\n", intro, "",
            "_(Edita esta nota manualmente à medida que registas trabalho.)_\n"]
    return Note(drawer=drawer, slug=slug, title=title, source=None,
                body="\n".join(body), tags=["placeholder"])


# ---------------------------------------------------------------------------
# ESCRITA NO VAULT
# ---------------------------------------------------------------------------

def ensure_vault(vault: Path) -> None:
    """Cria a estrutura de gavetas se não existir."""
    vault.mkdir(parents=True, exist_ok=True)
    for d, desc in DRAWERS.items():
        sub = vault / d
        sub.mkdir(exist_ok=True)
        index = sub / "_index.md"
        if not index.exists():
            index.write_text(
                f"---\ntitle: {d}\n---\n\n# {d}\n\n{desc}\n",
                encoding="utf-8",
            )


def write_note(vault: Path, note: Note, dry_run: bool = False) -> Path:
    target_dir = vault / note.drawer
    target_dir.mkdir(parents=True, exist_ok=True)
    target = target_dir / f"{note.slug}.md"
    rendered = note.render()
    if dry_run:
        print(f"  [dry-run] {target.relative_to(vault)}")
        return target

    # Hash para evitar reescrever se nada mudou (preserva timestamp)
    new_hash = hashlib.sha1(rendered.encode("utf-8")).hexdigest()
    if target.exists():
        old = target.read_text(encoding="utf-8")
        old_hash = hashlib.sha1(old.encode("utf-8")).hexdigest()
        if new_hash == old_hash:
            return target
    target.write_text(rendered, encoding="utf-8")
    return target


def clean_vault(vault: Path) -> None:
    """Apaga todas as gavetas geridas (preserva ficheiros fora delas)."""
    for d in DRAWERS:
        sub = vault / d
        if sub.exists():
            shutil.rmtree(sub)


# ---------------------------------------------------------------------------
# MAIN
# ---------------------------------------------------------------------------

def collect_notes() -> list[Note]:
    """Pipeline completo de geração."""
    notes: list[Note] = [gen_visao()]

    s = gen_settings()
    if s:
        notes.append(s)

    rotas_idx, rotas_sub = gen_urls()
    notes.extend([rotas_idx, *rotas_sub])

    views_idx, views_sub = gen_views()
    notes.extend([views_idx, *views_sub])

    notes.extend(gen_templates())
    notes.append(gen_assets())
    notes.append(gen_stack())

    notes.append(gen_placeholder(
        "sessoes", "sessoes-indice", "Sessões · Índice",
        "Regista aqui cada sessão de trabalho relevante."))
    notes.append(gen_placeholder(
        "erros", "erros-indice", "Erros · Índice",
        "Regista erros encontrados, causa raiz e resolução."))
    notes.append(gen_placeholder(
        "decisoes", "decisoes-indice", "Decisões · Índice",
        "Regista ADRs (Architecture Decision Records)."))

    return notes


def main() -> int:
    parser = argparse.ArgumentParser(description="Sincroniza docs do projecto para Obsidian.")
    parser.add_argument("--vault", type=Path,
                        default=Path(os.environ.get("OBSIDIAN_VAULT", DEFAULT_VAULT)),
                        help="Caminho do Vault Obsidian.")
    parser.add_argument("--dry-run", action="store_true", help="Mostra sem escrever.")
    parser.add_argument("--clean", action="store_true",
                        help="Apaga gavetas geridas antes de regenerar.")
    args = parser.parse_args()

    vault: Path = args.vault.expanduser().resolve()
    print(f"📚 Projecto: {PROJECT_ROOT}")
    print(f"🗄️  Vault:    {vault}")

    if args.clean and not args.dry_run:
        print("🧹 Limpando gavetas geridas...")
        clean_vault(vault)

    if not args.dry_run:
        ensure_vault(vault)

    notes = collect_notes()
    print(f"📝 Notas a gerar: {len(notes)}")

    # Verificação de slugs únicos
    seen: dict[str, str] = {}
    for n in notes:
        if n.slug in seen:
            print(f"⚠️  Slug duplicado: {n.slug} ({n.drawer} vs {seen[n.slug]})")
        seen[n.slug] = n.drawer

    written = 0
    for n in notes:
        write_note(vault, n, dry_run=args.dry_run)
        written += 1

    print(f"✅ {written} notas {'simuladas' if args.dry_run else 'escritas'} em {vault}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
