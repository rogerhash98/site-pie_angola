---
title: Sessão 2026-04-20 · Bootstrap do Vault Obsidian
drawer: sessoes
updated: 2026-04-20
tags: [sessao, vault, obsidian, automacao]
---

# Sessão · 2026-04-20 — Vault Obsidian + wiki_sync

## Objectivo
Criar memória de longo prazo para a IA via Obsidian: documentação `.md`
gerada automaticamente do código, organizada em gavetas semânticas,
versionável dentro do projecto.

## O que foi feito

### 1. Análise da base de código
- Mapeada estrutura: `app/` (Django), `templates/` (HTML), `static/`, `scripts/`.
- Identificadas 11 views, 11 rotas, 12 templates, 3 componentes, 2 produtos.

### 2. Definidas gavetas semânticas
12 pastas em `doc/` alinhadas com as instruções do agente:
`visao/`, `arquitectura/`, `rotas/`, `views/`, `templates/`,
`componentes/`, `produtos/`, `assets/`, `stack/`,
`sessoes/`, `erros/`, `decisoes/`.

### 3. Filtro de ruído implementado
Ignorados: `__pycache__`, `.git`, `.venv`, `node_modules`,
`migrations/`, `db.sqlite3`, `uv.lock`, `.env`, `asgi.py`,
`wsgi.py`, `manage.py`, binários, `__init__.py` vazios,
`scripts/`, `doc/` (auto-exclusão).

### 4. Script `scripts/wiki_sync.py`
- Python 3.10+ stdlib only (sem `pip install`).
- Parsing AST de `views.py` → 1 nota por função.
- Regex sobre `urls.py` (após `urlpatterns =`) → 1 nota por rota.
- Templates HTML → detecção de `{% extends %}` / `{% include %}` para
  wikilinks automáticos.
- **Idempotente**: hash SHA-1 evita reescrita desnecessária.
- Flags: `--dry-run`, `--clean`, `--vault`.

### 5. Vault no projecto (decisão)
Default = `PROJECT_ROOT / "doc"` em vez de pasta global do utilizador.
Cada projecto tem o seu cérebro local, versionável no Git. Ver
[[adr-001-doc-no-projecto]].

### 6. Conexão MCP Obsidian
Plugin *Local REST API* activado em `https://127.0.0.1:27124`.
Token Bearer fornecido pelo utilizador. Vault aberto sobre `doc/`.

## Resultados
- 46 notas geradas em 12 gavetas.
- Wikilinks resolvem globalmente → mover não quebra.
- `python3 scripts/wiki_sync.py` regenera tudo a partir do código.

## Aprendizagens chave
- **Slug global** > caminho relativo nos wikilinks → robusto a refactor.
- **AST** > regex para parsing Python → resiliente a formatação.
- **Hash de conteúdo** preserva `mtime` → Obsidian não marca tudo como "modificado".

## Próximos passos
- Adicionar `doc/` ao commit (memória versionada).
- Hook git pré-commit ou `Makefile` para auto-regenerar.
- Corrigir auth do MCP Obsidian (config da CLI).

## Relacionados
- [[adr-001-doc-no-projecto]]
- [[adr-002-wiki-sync-stdlib]]
- [[adr-003-slugs-wikilinks]]
- [[mcp-obsidian-auth]]
- [[estado-actual]]
