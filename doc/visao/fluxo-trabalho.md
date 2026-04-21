---
title: Fluxo de trabalho neste projecto
drawer: visao
updated: 2026-04-20
tags: [visao, fluxo, processo]
---

# Fluxo de trabalho — PIE Angola

Como trabalhar neste projecto sem repetir erros. Lê **antes** de
começar qualquer alteração.

## Antes de codar
1. **Consultar o Vault** (`doc/`) — ver se a abordagem já foi tentada.
2. Verificar [[stack-confirmada]] — não desviar sem ADR.
3. Ler [[erros/]] relevantes — não repetir.
4. Ver [[estado-actual]] — entender contexto.

## Durante a alteração
1. Mudanças cirúrgicas — não tocar em código não relacionado.
2. Após cada alteração de UI: **chrome-devtools** abre, valida 5 áreas:
   - Console (zero erros)
   - Network (sem 4xx/5xx inesperados)
   - Application (cookies/storage OK)
   - Performance (sem regressões)
   - Elements (DOM/estilos OK)
3. Para QA visual: comparar com Figma via Figma MCP.
4. Para validação cruzada: Playwright MCP + screenshot.

## Após terminar
1. Correr o servidor: `python manage.py runserver`.
2. Verificar logs Django (sem warnings de migração, sem 500s).
3. **Regenerar memória:** `python3 scripts/wiki_sync.py`.
4. Adicionar nota em `doc/sessoes/AAAA-MM-DD-<tema>.md` resumindo:
   - O que foi feito
   - O que funcionou (vira padrão)
   - O que NÃO funcionou (vira nota em `doc/erros/`)
5. Se decisão arquitectural: criar ADR em `doc/decisoes/adr-NNN-<tema>.md`.
6. Commit (memória + código juntos).

## Comandos úteis
```bash
# Servidor dev
python manage.py runserver

# Regenerar Vault
python3 scripts/wiki_sync.py

# Vault limpo + regenerado
python3 scripts/wiki_sync.py --clean

# Ver Vault no Obsidian
# File → Open folder as vault → ./doc

# Inspeccionar Vault via REST API
TOKEN="..." curl -sk -H "Authorization: Bearer $TOKEN" \
  https://127.0.0.1:27124/vault/
```

## Onde escrever cada coisa
| Tipo de info | Vai para |
|---|---|
| Estado/visão geral | `doc/visao/` |
| Como o código está estruturado | `doc/arquitectura/` (auto) |
| Sessão de trabalho | `doc/sessoes/AAAA-MM-DD-tema.md` |
| Decisão técnica | `doc/decisoes/adr-NNN-tema.md` |
| Erro encontrado + solução | `doc/erros/tema.md` |
| Stack confirmada | `doc/stack/` |
| Resto do código | regenerado automaticamente |

## Relacionados
- [[estado-actual]]
- [[stack-confirmada]]
- [[2026-04-20-vault-obsidian]]
