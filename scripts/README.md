# Wiki Sync — PIE Angola → `doc/` (Vault Obsidian local)

Script `wiki_sync.py` lê o código Django e gera documentação `.md`
organizada em **gavetas semânticas** dentro da pasta `doc/` do próprio
projecto. Cada projecto fica com o seu Vault local — versionável no Git
junto com o código.

## Por que `doc/` no projecto?

Alinhado com as instruções do agente para este repo:
> *Criar notas por tema: `doc/erros/`, `doc/decisoes/`, `doc/visao/`,
> `doc/stack/`, `doc/sessoes/`*

Vantagens:
- A documentação anda com o código (mesmo branch, mesmo PR).
- Cada projecto tem o seu próprio "cérebro" isolado.
- Abres a pasta `doc/` no Obsidian (`File → Open folder as vault`) e
  passa a ser o teu Vault desse projecto.

## Gavetas geradas

| Gaveta | Conteúdo |
|---|---|
| `doc/visao/` | MOC raiz + README |
| `doc/arquitectura/` | `app/settings.py` |
| `doc/rotas/` | `app/urls.py` (uma nota por rota) |
| `doc/views/` | `app/views.py` (uma nota por função) |
| `doc/templates/` | Páginas HTML de topo |
| `doc/componentes/` | `templates/components/` |
| `doc/produtos/` | `templates/products/` |
| `doc/assets/` | Inventário de `static/` |
| `doc/stack/` | `pyproject.toml`, versões |
| `doc/sessoes/` | Log manual (placeholder) |
| `doc/erros/` | Erros + resoluções (placeholder) |
| `doc/decisoes/` | ADRs (placeholder) |

## Filtro de ruído

Ignorados automaticamente:
`__pycache__`, `.git`, `.venv`, `node_modules`, `migrations/`,
`db.sqlite3`, `uv.lock`, `.env`, `asgi.py`, `wsgi.py`, `manage.py`,
binários (png/jpg/svg/woff/...), `__init__.py` vazios, `scripts/`,
`doc/` (o próprio Vault).

## Wikilinks

Cada nota tem **slug único prefixado** (`view-home`, `tpl-about`,
`cmp-menu`, `rota-contact`, ...). O Obsidian resolve `[[slug]]`
globalmente — reorganizar pastas no Vault **não quebra ligações**.

## Uso

```bash
# Geração para doc/ (default — não precisa de configurar nada)
python3 scripts/wiki_sync.py

# Simulação
python3 scripts/wiki_sync.py --dry-run

# Regeneração limpa (apaga gavetas geridas e regera)
python3 scripts/wiki_sync.py --clean

# Vault noutro local (override)
python3 scripts/wiki_sync.py --vault /caminho/alternativo
OBSIDIAN_VAULT=/outro/caminho python3 scripts/wiki_sync.py
```

Depois: abre `doc/` no Obsidian — `File → Open folder as vault`.

## Idempotência

Hash SHA-1 do conteúdo: notas inalteradas **não são reescritas**
(preserva o `mtime` que o Obsidian usa para "modificado").

## Versionamento

Recomendado **commitar** `doc/` no Git: a documentação acompanha o
código. Se preferires manter fora do repo, adiciona ao `.gitignore`:

```
doc/
```

## Requisitos

- Python 3.10+
- Apenas stdlib (sem `pip install`)
