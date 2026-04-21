---
title: MCP Obsidian · auth required
drawer: erros
date: 2026-04-20
status: contornado
tags: [erro, mcp, obsidian, auth]
---

# Erro · MCP Obsidian retorna 40101 "Authorization required"

## Sintoma
```
MCP server 'obsidian': Caught Exception.
Error 40101: Authorization required.
Find your API Key in the 'Local REST API' section of your Obsidian settings.
```

## Causa raiz
O servidor MCP `obsidian` (CLI) não tem o **Bearer token** configurado.
O plugin *Local REST API* do Obsidian responde em
`https://127.0.0.1:27124` mas exige `Authorization: Bearer <token>` em
todas as chamadas.

## Antes deste erro
```
HTTPSConnectionPool(host='127.0.0.1', port=27124):
Failed to establish a new connection: [Errno 111] Connection refused
```
→ Plugin estava desactivado. Resolvido ao activar *Local REST API* no
Obsidian (`Settings → Community plugins → Local REST API → enable`).

## Solução temporária (funciona)
Chamar a API directamente com `curl` passando o Bearer:
```bash
TOKEN="<token-do-plugin>"
curl -sk -H "Authorization: Bearer $TOKEN" \
  https://127.0.0.1:27124/vault/
```

`-k` é necessário porque o plugin usa cert auto-assinado.

## Solução definitiva (pendente)
Configurar o token no servidor MCP `obsidian` (provavelmente via env var
`OBSIDIAN_API_KEY` ou no ficheiro de config do servidor MCP). Verificar
docs do servidor MCP usado.

## Padrão aprovado
- Token vive **fora** do repo (env var ou keyring).
- Para automação local: `OBSIDIAN_API_KEY=... && python script.py`.
- **Nunca** commitar o token.

## Relacionados
- [[2026-04-20-vault-obsidian]]
- [[fluxo-trabalho]]
