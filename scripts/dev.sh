#!/usr/bin/env bash
# Modo desenvolvimento: HTTP simples, sem HTTPS forçado, sem HSTS.
# Uso: ./scripts/dev.sh [port]
set -euo pipefail
cd "$(dirname "$0")/.."

export DJANGO_DEBUG=True
unset DJANGO_SECURE_SSL_REDIRECT DJANGO_HSTS_SECONDS DJANGO_STATICFILES_BACKEND

PYTHON_BIN="${PYTHON_BIN:-$(command -v python3 || command -v python)}"
PORT="${1:-8000}"

"$PYTHON_BIN" manage.py migrate --noinput
exec "$PYTHON_BIN" manage.py runserver "127.0.0.1:${PORT}"
