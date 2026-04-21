---
title: Stack confirmada (funcional neste projecto)
drawer: stack
updated: 2026-04-20
tags: [stack, deps, confirmado]
---

# Stack confirmada — PIE Angola

Versões e configurações **confirmadas a funcionar** neste projecto.
Antes de mudar qualquer item desta lista: documentar a razão e criar ADR.

## Runtime
| Item | Versão | Notas |
|---|---|---|
| Python | ≥ 3.14 (declarado), 3.10+ funciona para o `wiki_sync` | `requires-python = ">=3.14"` em pyproject |
| Django | ≥ 6.0.3 | release recente, sem migrations app-level |
| SQLite | builtin | DB de dev (`db.sqlite3`) |
| Gestor de pacotes | `uv` | `uv.lock` no repo |

## Email
- `EMAIL_BACKEND = console` em dev (commit `3edb59f`).
- Em produção falta configurar SMTP real.

## Frontend
- **Sem framework JS** — HTML5 + CSS3 + JS vanilla.
- Templates Django puros (sem DRF, sem HTMX, sem Alpine).
- Static servido pelo Django em dev.

## Estrutura confirmada
```
app/
  settings.py    ← config Django
  urls.py        ← 11 rotas
  views.py       ← 11 funções (function-based views)
templates/
  *.html         ← páginas topo
  components/    ← menu, footer, help_chat
  products/      ← winrest_nx, pingwin_bo
static/
  css/ js/ images/
scripts/
  wiki_sync.py   ← gerador de doc
doc/             ← Vault Obsidian local
```

## Ferramentas auxiliares
- **Figma MCP** — referência visual canónica para QA.
- **Playwright MCP** — screenshots e validação visual (`.playwright-mcp/`).
- **Obsidian + Local REST API** — interface humana à memória.
- **GitHub MCP** — interacção com repo.

## Padrões aprovados (não mudar sem ADR)
- Views function-based (não class-based) — decisão estilística.
- Sem models até haver necessidade real (site institucional).
- Wiki gerada por `scripts/wiki_sync.py` (ver [[adr-002-wiki-sync-stdlib]]).
- Vault em `doc/` no projecto (ver [[adr-001-doc-no-projecto]]).

## Relacionados
- [[stack-pyproject]]
- [[arq-settings]]
- [[estado-actual]]
