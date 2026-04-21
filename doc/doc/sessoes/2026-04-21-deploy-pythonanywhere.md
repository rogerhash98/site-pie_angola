# Deploy PythonAnywhere — site PIE Angola

**Data:** 2026-04-21
**URL produção:** https://rochimuc.pythonanywhere.com/
**Repo deploy:** https://github.com/rogerhash98/site-pie_angola (público)
**Status:** ✅ Online, HTTPS forçado, footer Mirantes OK, logo PIE Angola OK

## Stack PA
- Free tier (512MB disco, 1 web app, subdomain `<user>.pythonanywhere.com`)
- Python 3.13 venv: `/home/rochimuc/.virtualenvs/pieangola`
- Source: `/home/rochimuc/site-pie_angola`
- WSGI: `/var/www/rochimuc_pythonanywhere_com_wsgi.py` (env vars hardcoded — free tier não tem painel env vars)
- Static mapping: `/static/` → `/home/rochimuc/site-pie_angola/staticfiles`
- DB: SQLite local em `db.sqlite3`

## Arquivos chave
- `deploy/pythonanywhere_setup.sh` — idempotente: clone/pull, venv, pip, migrate, collectstatic
- `deploy/pythonanywhere_wsgi.py` — template WSGI (copiar para /var/www/...)
- `app/settings.py` — lê `DJANGO_STATICFILES_BACKEND` env var

## Padrão aprovado
- **Storage estático SEM compressão whitenoise no PA free** (PA serve via Nginx)
  - env: `DJANGO_STATICFILES_BACKEND=django.contrib.staticfiles.storage.StaticFilesStorage`
  - Whitenoise compression triplica disco e estoura quota 512MB
- **Repo público** quando push HTTPS via gh CLI (conta SSH local pode diferir da gh CLI)
- **WSGI hardcoded SECRET_KEY** no /var/www/ (fora do repo) no free tier sem painel env vars

## Erros que NÃO repetir
- ❌ Whitenoise CompressedManifest no PA free → "Disk quota exceeded" durante collectstatic
- ❌ Repo privado em conta SSH ≠ conta gh CLI → console PA pede credenciais no `git clone`
- ❌ `sed` local no setup.sh + git pull → conflito; usar `git checkout -- .` antes de pull

## Chrome DevTools tricks
- Console PA hterm: enviar comandos via `evaluate_script` injetando `KeyboardEvent('keypress')` no textarea dentro de `iframe > iframe > textarea` (não usar `press_key` para strings)
- Editor Ace PA: `window.ace.edit(document.querySelector('.ace_editor')).setValue(content, -1)` + click Save

## Próximos passos
- Renovar deploy mensalmente (botão "Run until 1 month from today")
- Mudar para domínio próprio se necessário (paid tier)
- Backup periódico do `db.sqlite3`
