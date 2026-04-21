---
title: "Sessão — Scraping winrest360.com.ao"
date: 2026-04-21
tags: [sessao, scraping, winrest360, referencia]
---

# Scraping winrest360.com.ao → vault Obsidian

## Objectivo
Capturar conteúdo de referência do site institucional **WinRest360 Angola** para servir de fonte secundária ao actualizar copy do projecto Django PIE Angola.

## Entregáveis
- Script: `scripts/scrape_winrest360.py` (Python stdlib + bs4 + lxml)
- Saída: `doc/scraping/winrest360-ao/` (9 notas + `_index.md`)

## Resultado
- Páginas no sitemap: **15**
- Capturadas com sucesso: **9**
- Falharam (HTTP 500 do servidor remoto): **6**

### Notas capturadas
- [[index]] — home
- [[a-empresa]]
- [[linkya]]
- [[modulos-adicionais]]
- [[o-que-e-o-winrest-360]]
- [[track-in-time]]
- [[winorder]]
- [[winrest-booking]]
- [[winrest-nx]]

### Páginas com HTTP 500 (servidor)
Confirmado com `curl` directo + UA browser-like + 4 retries com backoff. Não é anti-bot, são páginas genuinamente quebradas no servidor de origem:
- `/a-quem-se-destina/`
- `/como-funciona/`
- `/fornecedores-alimentares/`
- `/funcionalidades/`
- `/que-problemas-resolve/`
- `/uma-solucao-a-custo-zero/`

## Stack do alvo
WordPress + Elementor + Yoast SEO. Sitemap em `https://ao.winrest360.com/sitemap.xml` → `page-sitemap.xml`.

## Como refrescar
```bash
uv run python scripts/scrape_winrest360.py
```

## Próximos passos
- Tentar de novo as 6 URLs após algum tempo (servidor pode recuperar).
- Considerar fallback via Wayback Machine para conteúdo das 6 páginas em falta.
- Não promover a memória "fonte de verdade": é apenas referência externa de concorrente/parceiro.
