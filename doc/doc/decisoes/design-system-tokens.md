# Design System — tokens.css + base.html

**Data**: refactor 2026-04 · **Commit**: `a419aba`

## Decisão
Adoptar design system com CSS variables (`tokens.css`) extraídas do site PIE Portugal (https://wwwpp.grupopie.com/) + Figma `0Gu9ADLtBcGiPk7gE8lAPG`. Eliminar boilerplate `<head>` duplicado em 11 templates via `base.html` com Django template inheritance.

## Tokens chave (extraídos do PT real)
- **Brand red**: `#c93131` (`rgb(201,49,49)`) — confirmado em CTA + section markers
- **Body text**: `#37393f` (`rgb(55,57,63)`) — paragraphs, nav links
- **Title hero**: `#000000` 48px Inter 700 line-height 55px
- **CTA primary**: `bg #c93131`, padding `12px 35px`, radius `8px`, font 18px
- **Outlined button**: padding `15px 60px`, border `0.8px solid #c93131`, radius `10px`, font 18px/600
- **Nav**: 18px Inter 400 (`#37393f`)
- **Container**: max 1280px, gutters 48px desktop
- **Header height**: 96px
- **Family**: Inter (preferido), Cabin (display secundário)

## base.html — blocks expostos
- `title`, `description`, `body_class`, `head_extra`, `content`, `scripts`
- Inclui por defeito: menu, footer, help_chat, main.js, help_chat.js, tokens.css, styles.css, menu.css, help_chat.css

## Migração 11 templates
Script Python (`/tmp/templates-backup/` tem o original) extraiu:
- `<title>` → `{% block title %}`
- `<meta description>` → `{% block description %}`
- `<body class>` → `{% block body_class %}`
- CSS extras (não-padrão) → `{% block head_extra %}`
- Conteúdo entre menu/footer includes → `{% block content %}`
- Scripts custom → `{% block scripts %}`

Resultado: -259 +234 lines, ~170 linhas de boilerplate eliminadas.

## Smoke test pós-migração
Todas as 9 rotas públicas → HTTP 200:
`/`, `/sobre-nos/`, `/solucoes/`, `/recrutamento/`, `/casos-de-sucesso/`, `/produtos/winrest-nx/`, `/produtos/pingwin-bo/`, `/clientes/`, `/contacto/`

## Próximos passos
- Fase 1: criar atoms/molecules/organisms
- Refinar header/footer com medidas exactas PT
- Páginas: home → soluções → produtos → casos → resto
