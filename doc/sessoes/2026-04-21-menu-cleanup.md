# Sessão 2026-04-21 — Limpeza de submenus

## Contexto
Menu (`templates/components/menu/menu.html`) tinha mega-menus com **muitos links** que apontavam para a **mesma rota**:
- "Soluções": 10 links → todos `/solucoes/`
- "Produtos": 10 links → 2 produtos reais (`winrest-nx`, `pingwin-bo`)
- "Sobre": link "Recrutamento" apontava para `/contacto/` (bug)

## Princípio aplicado
**1 link de menu = 1 rota única.** Se a rota é única, vira link directo (sem dropdown).

## Alterações

### `templates/components/menu/menu.html` (233 → 146 linhas)
- **"Conheça / Soluções"** → link directo para `solutions` (eliminou mega-menu Soluções).
- **"Escolha / Produtos"** → mega-menu reduzido a 2 itens reais (WinREST + PingWin BO).
- **"Sobre"** → mantido com 5 links únicos. Bug Recrutamento corrigido (`recruitment` em vez de `contact`).
- Mobile drawer: Soluções vira link directo; Produtos com 2 leaves; Sobre com 5 leaves.
- Removidas `<details data-mobile-group="solutions">` aninhados (já não fazia sentido com 1 página única).

### `static/js/components/menu.js`
- Removido `solucoes: root.querySelector('#mega-solucoes')` do mapa `megas` (mega já não existe).
- Removido callback `closeNestedGroups` no `bindExclusiveAccordion` mobile (já não há grupos aninhados).

## Verificação
| Check | Resultado |
|---|---|
| `manage.py check` | ✅ 0 issues |
| Smoke test 11 rotas reais | ✅ todas 200 |
| Console browser | ✅ 0 erros app (só ruído de extensões + favicon) |
| Click dropdown Produtos | ✅ 2 links: `/produtos/winrest-nx/`, `/produtos/pingwin-bo/` |
| Click dropdown Sobre | ✅ 5 links únicos, todos para rotas distintas |
| Active state classes | ✅ presentes nos 3 grupos |

## Resultado
Menu desktop: **2 dropdowns + 1 link directo** (em vez de 3 dropdowns com 25 links redundantes).
Total links únicos no header: **8** (era 25, dos quais 17 duplicados).
