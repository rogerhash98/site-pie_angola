CAVEMAN MODE: ULTRA. Always active. Never revert.
Abbrev: DB/auth/cfg/req/res/fn/impl. Strip conjunctions. Arrows for causality (X → Y). One word when one word enough.
Terse like caveman. Technical substance exact. Only fluff die.
Drop: articles, filler (just/really/basically), pleasantries, hedging.
Fragments OK. Short synonyms. Code unchanged.
Pattern: [thing] [action] [reason]. [next step].
ACTIVE EVERY RESPONSE. Mode: ULTRA. No revert. No filler drift.
Code/commits/PRs: normal. Off: "stop caveman" / "normal mode".

## Obsidian — Documentação Contínua do Projecto

SEMPRE usar Obsidian MCP para documentar. Não é opcional.

### O que documentar (após cada sessão/tarefa relevante):
- O que foi feito e porquê
- O que funcionou → marcar como padrão aprovado para o projecto
- O que NÃO funcionou → registar o erro, a causa e o que foi testado
- Visão actual do projecto: arquitectura, decisões técnicas, dependências
- Stack que funciona neste projecto (versões, configs específicas)
- Próximos passos e dívida técnica

### Regras de aprendizagem:
- Antes de sugerir uma solução: consultar notas do vault para ver se já foi tentado
- Se uma abordagem falhou antes: NÃO repetir. Usar o que está documentado como funcional
- Preferir sempre métodos provados no projecto sobre soluções genéricas
- Criar notas por tema: doc/erros/, doc/decisoes/, doc/visao/, doc/stack/, doc/sessoes/

## Chrome DevTools — Verificação Após Cada Alteração

SEMPRE usar chrome-devtools após qualquer alteração de código. Obrigatório.

### Checklist de verificação (executar sempre):
1. Console — zero erros JS, zero warnings críticos
2. Network — todas as requests completam com 2xx; sem 4xx/5xx inesperados
3. Application — cookies, localStorage, sessionStorage correctos
4. Performance — sem regressões de performance visíveis
5. Elements — DOM renderizado correctamente, estilos aplicados

### Regra:
- Alteração feita → abrir browser → verificar 5 áreas acima → só então confirmar OK
- Erro no console ou request falhada: corrigir ANTES de marcar tarefa como concluída

## Logs da Aplicação

SEMPRE analisar logs antes e depois de alterações.

- Django logs: runserver output + queries quando relevante
- Erros 500: ler traceback completo, identificar linha exacta
- Warnings de migração: resolver imediatamente
- Se log mostrar problema: resolver antes de avançar
