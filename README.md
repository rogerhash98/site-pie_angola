# PIE Angola — Site Institucional

Django 6.x. Deploy em produção: PythonAnywhere — https://rochimuc.pythonanywhere.com/

## Modos

### Desenvolvimento (default)
HTTP simples, sem HTTPS forçado, sem HSTS, sem cookies seguros.

```bash
pip install -r requirements.txt
./scripts/dev.sh          # http://127.0.0.1:8000
```

Equivalente:
```bash
export DJANGO_DEBUG=True
python manage.py migrate
python manage.py runserver
```

### Produção
`DJANGO_DEBUG=False` activa SECURE_SSL_REDIRECT, HSTS, cookies seguros, WhiteNoise comprimido com manifest.

Local (gunicorn):
```bash
export DJANGO_SECRET_KEY=...
./scripts/prod.sh          # http://127.0.0.1:8001
```

PythonAnywhere: ver `deploy/pythonanywhere_wsgi.py` e `deploy/pythonanywhere_setup.sh`.

## Browser cacheou HSTS de localhost?

Se ao executar `runserver` o browser tenta HTTPS automático em `127.0.0.1:8000` (logs com `Bad request version` / `accessing development server over HTTPS`):

- Chrome: `chrome://net-internals/#hsts` → "Delete domain security policies" → `localhost` e `127.0.0.1`
- Ou usar janela anónima
- Ou outro browser

## Variáveis de ambiente

Ver `.env.example`.

## Estrutura

- `app/` — settings, urls, wsgi
- `pages/` — views, models, urls do site
- `templates/` — HTML (sem base.html, head próprio em cada template)
- `static/` — CSS, JS, imagens
- `deploy/` — scripts e WSGI para PythonAnywhere
- `scripts/` — `dev.sh`, `prod.sh`, scrapers
- `doc/` — vault Obsidian (decisões, sessões, erros, stack)
