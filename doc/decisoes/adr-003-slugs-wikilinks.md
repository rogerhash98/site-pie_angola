---
title: ADR-003 · Slugs únicos prefixados para wikilinks
drawer: decisoes
date: 2026-04-20
status: aceite
tags: [adr, obsidian, wikilinks]
---

# ADR-003 — Slugs únicos prefixados para wikilinks

## Contexto
Wikilinks Obsidian podem usar:
- `[[caminho/relativo/nota]]` — frágil, quebra ao mover.
- `[[nome-da-nota]]` — Obsidian resolve globalmente.

## Decisão
Cada nota tem **slug único prefixado por categoria**:
- `view-{nome}` — funções de view
- `rota-{nome}` — rotas URL
- `tpl-{nome}` — templates página
- `cmp-{nome}` — componentes
- `prod-{nome}` — produtos
- `arq-{nome}` — arquitectura
- `stack-{nome}` — stack

## Justificação
- Reorganizar pastas no Vault **não quebra ligações**.
- Prefixo evita colisões (ex: existe `home` como rota E como template).
- Auto-completion no Obsidian agrupa por prefixo (digitas `view-` →
  vês todas as views).

## Padrão aprovado
```python
def slugify(value: str) -> str:
    value = re.sub(r"[^\w\-]+", "-", value.lower()).strip("-")
    return re.sub(r"-+", "-", value) or "untitled"

slug = f"{prefix}-{slugify(name)}"
```

## Falsos positivos detectados e resolvidos
- Regex de URLs apanhava exemplos do **docstring** de `urls.py`.
  - **Causa:** `re.findall` sobre o ficheiro inteiro.
  - **Fix:** `content.split("urlpatterns =", 1)[-1]` antes do regex.
  - Ver [[mcp-obsidian-auth]] para outros casos similares.

## Relacionados
- [[adr-001-doc-no-projecto]]
- [[adr-002-wiki-sync-stdlib]]
