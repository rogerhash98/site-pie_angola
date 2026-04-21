#!/usr/bin/env bash
# Modo produção local: gunicorn, DEBUG=False, sem SSL redirect (proxy externo).
# Para deploy real ver deploy/pythonanywhere_wsgi.py.
# Uso: ./scripts/prod.sh [port]
set -euo pipefail
cd "$(dirname "$0")/.."

export DJANGO_DEBUG=False
export DJANGO_SECURE_SSL_REDIRECT="${DJANGO_SECURE_SSL_REDIRECT:-False}"
export DJANGO_ALLOWED_HOSTS="${DJANGO_ALLOWED_HOSTS:-127.0.0.1,localhost}"
: "${DJANGO_SECRET_KEY:?DJANGO_SECRET_KEY obrigatória em produção}"

PYTHON_BIN="${PYTHON_BIN:-$(command -v python3 || command -v python)}"
PORT="${1:-8001}"

"$PYTHON_BIN" manage.py collectstatic --noinput
"$PYTHON_BIN" manage.py migrate --noinput
exec "$PYTHON_BIN" -m gunicorn app.wsgi:application --bind "127.0.0.1:${PORT}" --workers 3
