# Localização da PIE Angola

## Endereço actual (confirmado)

**Condomínio Mirantes de Talatona**
Município do Talatona, Província de Luanda, Angola

> Nota: Talatona pertence administrativamente ao Município de Belas. O endereço antigo no site pieangola.com refere "Rua A nº 8 / Rua B nº 18, Bairro Militar, Município de Belas" — está desactualizado em relação à localização actual confirmada.

## Coordenadas

| Formato | Valor |
|---|---|
| DMS | 8°54'32.2"S 13°11'51.4"E |
| Decimal | **-8.908944, 13.197611** |
| Plus Code (curto) | 35RX+C2H Belas |
| Plus Code (global) | 5GR935RX+C2H |

## Verificação

Confirmado via OpenStreetMap Nominatim (reverse geocoding):

```json
{
  "display_name": "Condomínio Mirantes de Talatona, Talatona, Município do Talatona, Luanda, Angola",
  "address": {
    "residential": "Condomínio Mirantes de Talatona",
    "suburb": "Talatona",
    "county": "Município do Talatona",
    "state": "Luanda",
    "country": "Angola",
    "country_code": "ao"
  },
  "osm_type": "way",
  "osm_id": 385072459
}
```

## Links úteis

- OpenStreetMap: https://www.openstreetmap.org/?mlat=-8.908944&mlon=13.197611&zoom=18
- Google Maps: https://www.google.com/maps/place/8%C2%B054'32.2%22S+13%C2%B011'51.4%22E/@-8.908944,13.197611,18z
- Plus Codes: https://plus.codes/5GR935RX+C2H

## Uso no projecto

Usar estas coordenadas/endereço em:
- Rodapé do site (secção contactos)
- Schema.org `LocalBusiness` / `Organization` → `address` + `geo`
- Mapa embutido (Leaflet/OpenStreetMap ou Google Maps embed)
- Meta tags Open Graph com `og:latitude` e `og:longitude`

## Snippet schema.org sugerido

```json
{
  "@context": "https://schema.org",
  "@type": "Organization",
  "name": "PIE Angola, Lda",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "Condomínio Mirantes de Talatona",
    "addressLocality": "Talatona",
    "addressRegion": "Luanda",
    "addressCountry": "AO"
  },
  "geo": {
    "@type": "GeoCoordinates",
    "latitude": -8.908944,
    "longitude": 13.197611
  }
}
```
