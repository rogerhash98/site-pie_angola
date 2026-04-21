---
title: ADR-002 · wiki_sync em Python stdlib
drawer: decisoes
date: 2026-04-20
status: aceite
tags: [adr, automacao, python]
---

# ADR-002 — wiki_sync em Python stdlib only

## Contexto
Precisamos de um script que gere a documentação automaticamente a
partir do código. Opções consideradas:

1. **Sphinx / MkDocs** — gerador de docs maduro.
2. **Bash / PowerShell** — scripts shell.
3. **Node.js** — ecossistema rico de parsers.
4. **Python stdlib** — sem dependências extra.

## Decisão
Python 3.10+ usando apenas a biblioteca padrão (`ast`, `re`, `pathlib`,
`hashlib`, `argparse`).

## Justificação
- O projecto **já é Django** → Python disponível em qualquer máquina dev.
- **Zero `pip install`** → o script corre sempre, mesmo sem `.venv`.
- Módulo `ast` faz parsing fiável de `views.py` (resiste a formatação).
- Sphinx/MkDocs geram HTML estático — queremos **Markdown editável**
  no Obsidian, não site.

## Consequências
### Positivas
- Fácil de auditar (~440 linhas).
- Sem conflitos de dependências.
- Funciona em CI sem setup.

### Negativas
- Templating manual (em vez de Jinja). Aceita-se: poucos formatos.
- Sem hot-reload.

## Padrões aprovados
- Parsing Python: `ast.parse` + `ast.get_source_segment`.
- Slug seguro: `re.sub(r"[^\w\-]+", "-", value.lower())`.
- Idempotência: SHA-1 do conteúdo renderizado vs ficheiro existente.

## Relacionados
- [[adr-001-doc-no-projecto]]
- [[adr-003-slugs-wikilinks]]
