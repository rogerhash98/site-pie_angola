# Sessão Deploy — Fly.io (BLOQUEADO)

**Data:** 2026-04-21
**Status:** Configs prontas, deploy bloqueado por payment method

## O que foi feito

### Configs de produção criadas e commitadas (commit `a05311b`)
- **`Dockerfile`** — Python 3.12-slim, instala `requirements.txt` (inclui gunicorn 25 + whitenoise 6.12), `collectstatic` no build, `CMD` faz `migrate` + `gunicorn app.wsgi:application --bind 0.0.0.0:${PORT} --workers 3`
- **`.dockerignore`** — exclui `.git`, `.venv`, `__pycache__`, `staticfiles`, `db.sqlite3`, `.playwright-mcp`, `doc`, `scripts`
- **`fly.toml`** — app `site-pie-angola`, region `jnb` (Joanesburgo, mais perto de Angola), port 8080, http_service force_https + auto_stop_machines, healthcheck `/`, **volume mount `/data`** p/ persistir SQLite, env vars produção (`DJANGO_DEBUG=False`, `DJANGO_ALLOWED_HOSTS`, `DJANGO_CSRF_TRUSTED_ORIGINS`, `DJANGO_DB_PATH=/data/db.sqlite3`), 512MB shared CPU
- **`app/settings.py`** reescrito env-driven:
  - `SECRET_KEY` ← `DJANGO_SECRET_KEY`
  - `DEBUG` ← `DJANGO_DEBUG`
  - `ALLOWED_HOSTS` ← `DJANGO_ALLOWED_HOSTS` (default `localhost,127.0.0.1,.fly.dev`)
  - `CSRF_TRUSTED_ORIGINS` ← `DJANGO_CSRF_TRUSTED_ORIGINS`
  - `DATABASES.default.NAME` ← `DJANGO_DB_PATH`
  - WhiteNoise middleware + `CompressedManifestStaticFilesStorage`
  - Bloco `if not DEBUG:` c/ HSTS, SSL redirect, secure cookies, `SECURE_PROXY_SSL_HEADER`
  - `LANGUAGE_CODE='pt'`, `TIME_ZONE='Africa/Luanda'`, `DEFAULT_AUTO_FIELD='BigAutoField'`
- **`requirements.txt`** regenerado via `uv export` — agora inclui gunicorn 25.3.0 + whitenoise 6.12.0
- **`pyproject.toml`** + `uv.lock` actualizados via `uv add gunicorn whitenoise`

### Validação local
- `python manage.py check --deploy` → 2 warnings cosméticos (SECRET_KEY length em dev, HSTS_PRELOAD opcional). Sem erros.
- `collectstatic --noinput` → 250 files copiados, 610 post-processados (WhiteNoise compress). OK.

### Deploy via Chrome DevTools no dashboard Fly
- Logado como `franciscogama99@outlook.com`
- Form preenchido: repo `RogerioChimuco/site-pie_angola`, commit `a05311b`, branch `main`, app `site-pie-angola`, region `jnb`, port 8080, memory 512MB
- Env var `DJANGO_SECRET_KEY` adicionada como secret
- Clicado **Deploy** → resposta: **"Failed to create app. Please try again."**

## Bloqueio identificado

Banner persistente no dashboard:
> "Add a payment method to keep using our platform. To start deploying apps you'll need to add a payment method."

→ Link checkout: `https://fly.io/organizations/franciscogama99-outlook-com/payg-checkout?return_to=%2Fdashboard%2Ffranciscogama99-outlook-com`

**Fly.io removeu o free tier sem cartão (~2024).** Mesmo o plano hobby/pay-as-you-go exige cartão antes de qualquer deploy. Tentativa de bypass via API tokens não viável neste fluxo.

## Alternativas avaliadas

| Plataforma | Cartão? | Suporta Django nativo | Free tier real |
|------------|---------|----------------------|----------------|
| **Fly.io**  | **Sim, obrigatório** | Sim | Não (free era PAYG c/ crédito) |
| Render | Sim, obrigatório p/ web services | Sim | Sim (com cartão) |
| Koyeb | Sim agora | Sim | Não |
| Railway | Sim p/ trial | Sim | Não |
| **PythonAnywhere** | **Não** | **Sim** | **Sim (free Beginner)** |
| Vercel | Não | Não bem (serverless) | Sim mas inadequado |
| GitHub Pages | Não | Não (só estático) | Sim mas inadequado |

## Recomendação

### Opção A — Continuar com Fly.io (recomendada se cartão disponível)
1. Adicionar cartão em https://fly.io/organizations/franciscogama99-outlook-com/payg-checkout
2. Voltar ao dashboard, clicar Launch (configs já prontas, deploy single-click)
3. App ficará em `https://site-pie-angola.fly.dev`
4. Custo: ~$0/mês com auto-stop (machine dorme quando ocioso)

### Opção B — PythonAnywhere (sem cartão)
1. Criar conta free `Beginner` em https://www.pythonanywhere.com
2. Web app Django manual (não há git deploy automático no free)
3. Limitação: sem domínio próprio (`<user>.pythonanywhere.com`), sem WebSockets, 512MB disco
4. Adaptação necessária: `wsgi.py` config, sem Dockerfile

## Próximos passos (quando user voltar)

1. Decisão: cartão no Fly OU PythonAnywhere OU outra plataforma
2. Se Fly: clicar Launch (5 min para deploy + healthcheck)
3. Se PythonAnywhere: criar conta + adaptar deploy (sem Dockerfile, usar manage.py directamente)

## Decisões técnicas a manter (qualquer plataforma)

- ✅ env-driven settings (SECRET_KEY, DEBUG, ALLOWED_HOSTS, DB_PATH)
- ✅ WhiteNoise para serving static (sem CDN dependente)
- ✅ CompressedManifestStaticFilesStorage (cache busting + gzip)
- ✅ Security headers em produção (HSTS, SSL redirect, secure cookies)
- ✅ TIME_ZONE='Africa/Luanda' (correcto p/ utilizadores Angola)
- ⚠️ SQLite ephemeral aceitável só com volume persistente — sem volume, contact form perde dados a cada redeploy
