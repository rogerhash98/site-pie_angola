---
title: Estado actual do projecto
drawer: visao
updated: 2026-04-20
tags: [visao, estado, snapshot]
---

# Estado actual — PIE Angola

Snapshot manual — site institucional Django, fase de QA visual + integração Figma.

## Branch
`main` @ `9df9602` — *feat(home): transform hero into 2-slide carousel (WinRest + 360City FUN)*

## Páginas em produção (templates funcionais)
- [[tpl-home]] — homepage com carrossel hero 2 slides
- [[tpl-about]] — sobre nós
- [[tpl-solutions]] — soluções
- [[tpl-contact]] · [[tpl-contact_success]] — formulário de contacto + thank-you
- [[tpl-clients]] — clientes
- [[tpl-success_cases]] · [[tpl-success_case_detail]] — casos de sucesso
- [[tpl-recruitment]] — recrutamento
- [[prod-winrest_nx]] · [[prod-pingwin_bo]] — páginas de produto

## Componentes
- [[cmp-menu]] — header/nav com logo SVG (Figma node 14:1500)
- [[cmp-footer]] — footer light theme
- [[cmp-help_chat]] — widget de chat de ajuda (novo)

## Backend (mínimo, sem models)
- [[arq-settings]] — Django 6 + SQLite dev + EMAIL_BACKEND console
- [[rotas-urlconf]] — 11 rotas mapeadas
- [[views-indice]] — 11 views (todas function-based, render-only excepto `contact` POST)

## Trabalho recente confirmado (git log)
1. Hero homepage redesenhado como carrossel
2. Logo do menu unificado num SVG do Figma
3. Visual QA completo contra specs Figma
4. Footer light theme + cards de notícias com imagens únicas
5. Página de contacto redesenhada (Figma node 4435-6658)
6. Email backend = console (dev)

## Em progresso (git status)
- Modificações em todos os templates principais e CSS/JS de menu/styles
- Novos assets em `static/images/components/`
- `doc/` + `scripts/` (este sistema de memória)

## Pontos de entrada
- [[moc-pieangola]] — MOC raiz
- [[stack-confirmada]] — stack que funciona
- [[fluxo-trabalho]] — como trabalhar neste projecto

## Relacionados
- [[adr-001-doc-no-projecto]]
- [[adr-002-wiki-sync-stdlib]]
- [[adr-003-slugs-wikilinks]]
