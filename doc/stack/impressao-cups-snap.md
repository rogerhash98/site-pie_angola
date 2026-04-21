---
title: "Stack — Impressão (CUPS snap + IPP directo)"
date: 2026-04-21
tags: [stack, cups, impressora, ipp, snap]
---

# Impressão neste sistema

## Contexto
- CUPS instalado como **snap** (`/snap/cups/current/`)
- Comandos têm prefixo: `cups.lp`, `cups.lpstat`, `cups.lpadmin`, `cups.ipptool`, `cups.lpinfo`
- O `lpstat` do sistema (`/usr/bin/lpstat`) **não vê** as queues do snap → sempre usar `cups.*`

## Impressoras descobertas (mDNS / driverless)
| Nome                                  | IP             | MAC                 |
| ------------------------------------- | -------------- | ------------------- |
| HP LaserJet 600 M603 [031843]         | 192.168.1.70   | `2c:44:fd:03:18:43` |
| HP DeskJet 3830 series [8376A5]       | 192.168.1.230  | `10:e7:c6:83:76:a5` |

Resolver IP de impressora mDNS:
```bash
ip neigh | grep <últimos-bytes-do-serial>
```

## Bug conhecido — PPD everywhere
`cups.lpadmin -m everywhere` falha para a M603 com:
```
Printer returned invalid data: "media-default": Bad keyword value ""
```
PPD generator do cups-filters 2.0.1 dentro do snap não lida com resposta IPP da M603. **Não tentar registar como queue permanente por aqui.**

## Padrão funcional — imprimir via IPP directo

Ficheiro deve estar em `$HOME` (snap não acede `/tmp` do host).

```bash
cp /caminho/qualquer.pdf ~/print.pdf

cat > ~/print.test <<EOF
{
  OPERATION Print-Job
  GROUP operation-attributes-tag
  ATTR charset attributes-charset utf-8
  ATTR naturalLanguage attributes-natural-language en
  ATTR uri printer-uri \$uri
  ATTR name requesting-user-name \$user
  ATTR mimeMediaType document-format application/pdf
  FILE $HOME/print.pdf
  STATUS successful-ok
}
EOF

cups.ipptool -tv "ipp://192.168.1.70:631/ipp/print" ~/print.test
```

Resposta esperada: `[PASS]` + `job-state = processing`.

## Verificar estado de um job
```bash
cat > ~/status.test <<'EOF'
{
  OPERATION Get-Job-Attributes
  GROUP operation-attributes-tag
  ATTR charset attributes-charset utf-8
  ATTR naturalLanguage attributes-natural-language en
  ATTR uri printer-uri $uri
  ATTR integer job-id 5
  STATUS successful-ok
}
EOF
cups.ipptool -tv "ipp://192.168.1.70:631/ipp/print" ~/status.test
```

## Aprendizagens
- **Não usar `sudo lpadmin`** — opera no CUPS do sistema, que está vazio. Ignora o snap.
- **Não usar `cups.lp -d <nome>`** com queues temporárias detectadas em `cups.lpstat -e` — devolve "printer does not exist". Só funciona com queues registadas.
- **Funciona**: bypass total via `cups.ipptool` directo ao IP da impressora.

## Teste validado
2026-04-21 — Job 5 enviado a M603, aceite (`job-state=processing`), sem `job-state-reasons`.
