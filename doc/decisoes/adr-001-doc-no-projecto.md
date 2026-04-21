---
title: ADR-001 · Vault Obsidian dentro do projecto (`doc/`)
drawer: decisoes
date: 2026-04-20
status: aceite
tags: [adr, vault, organizacao]
---

# ADR-001 — Vault Obsidian dentro do projecto

## Contexto
Precisamos de memória persistente para a IA: documentação Markdown que
acompanha o código. Duas opções:

1. **Vault global** num único local (ex: `~/Obsidian/`) com todos os projectos.
2. **Vault por projecto** dentro da pasta do código (`./doc/`).

## Decisão
Vault local em `doc/` dentro de cada projecto.

## Justificação
- Documentação **versionada com o código** (mesmo branch, mesmo PR).
- Isolamento total entre projectos — sem contaminação cruzada.
- Clones do repo trazem a memória junto.
- Alinhado com as instruções do agente:
  *"Criar notas por tema: doc/erros/, doc/decisoes/, doc/visao/, ..."*

## Consequências
### Positivas
- Memória "viaja" com o código.
- Reviews de PR podem incluir actualizações de doc.
- Histórico Git mostra evolução da memória.

### Negativas
- Repete-se o `wiki_sync.py` por projecto (aceita-se: cada projecto tem
  parsing específico).
- `doc/` polui ligeiramente a árvore do projecto.

## Alternativas rejeitadas
- Vault global → contamina todos os projectos, perde-se contexto.
- Wiki externa (GitHub Wiki, Notion) → não funciona offline, fricção alta.

## Relacionados
- [[adr-002-wiki-sync-stdlib]]
- [[adr-003-slugs-wikilinks]]
- [[2026-04-20-vault-obsidian]]
