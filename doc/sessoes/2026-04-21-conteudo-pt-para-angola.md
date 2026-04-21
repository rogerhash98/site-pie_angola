---
data: 2026-04-21
tipo: sessao
tema: conteudo, marca, footer, contactos
status: concluido
---

# Sessão — Atualização de conteúdo PIE Portugal → PIE Angola

## Objetivo
Substituir dados remanescentes da PIE Portugal pelos dados oficiais da PIE Angola
(scraping em `doc/scraping/pieangola/`), mantendo layout intacto.

## Alterações aplicadas

### `templates/components/footer/footer.html`
- Bloco contacto telefone (`+351 …`) → bloco **Endereço** com pin SVG:
  - `Rua A nº 8 / Rua B nº 18`
  - `Bairro Militar, Município de Belas — Luanda, ANGOLA`
- Emails: `geral@grupopie.com` → `geral@pieangola.com`; `comercial@grupopie.com` → `comercial@pieangola.com`
- Copyright: `GrupoPIE Portugal SA` → `PIE Angola`

### `templates/contact.html`
- 2 office cards (Lisboa + Póvoa de Varzim) substituídos por:
  - **Luanda (Sede)** — endereço completo + iframe Maps Talatona
  - **Apoio & Assistência** — emails geral / comercial / info @pieangola.com

### `templates/about.html`
- Parágrafo "Quem é" reescrito para contexto Angola, mantendo referência ao GrupoPIE como marca-mãe (1995).

### `templates/home.html`
- `<title>` e `<meta description>` atualizados para "PIE Angola — Soluções globais para a restauração e retalho".

## Decisões registadas

1. **Telefone** → não há número Angola disponível no scraping. Bloco "Contactos" foi reaproveitado para "Endereço". Quando o user fornecer número real, substituir.
2. **Convenção de email** → `@pieangola.com` (consistente com `app/views.py` e `app/settings.py`).
3. **GrupoPIE como marca-mãe** → mantido em about/menu/breadcrumbs/help_chat por legitimidade da herança da marca; só substituído onde representava entidade jurídica portuguesa (copyright, escritórios).
4. **Social URLs** (`facebook.com/grupopie`, etc.) → não alteradas. Aguardar confirmação de contas oficiais @pieangola.

## Verificação
- Footer (home): endereço Luanda + emails @pieangola + copyright "PIE Angola" ✅
- /contacto/: 2 cards (Sede + Apoio) com mapas Luanda/Talatona ✅
- /sobre-nos/: parágrafo PIE Angola visível ✅
- Console: sem novos erros (apenas pré-existentes 404 + deprecation)

## Pendente
- Telefone Angola real (aguardar input user)
- URLs sociais (aguardar confirmação)


---

## Correção 2026-04-21 (endereço actualizado)

Endereço scraped antigo (Rua A nº 8, Bairro Militar) **descartado** — está desactualizado conforme `visao/localizacao-empresa.md`.

Endereço actual aplicado em footer + contact:
- **PIE Angola, Lda**
- **Condomínio Mirantes de Talatona**
- Talatona, Município do Talatona — Luanda, ANGOLA
- Iframe Maps usa coords -8.908944, 13.197611 (Plus Code 5GR935RX+C2H)

Fonte: `visao/localizacao-empresa.md` (confirmado via OSM Nominatim).
Lição: SEMPRE consultar Obsidian (`visao/`) antes de aplicar dados de scraping — scraping pode estar obsoleto.
