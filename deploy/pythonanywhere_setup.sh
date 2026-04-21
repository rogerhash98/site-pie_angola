#!/usr/bin/env bash
# Script de setup inicial para deploy em PythonAnywhere (free tier).
# Executa este script numa Bash console do PythonAnywhere.
#
# Uso:
#   bash ~/site-pie_angola/deploy/pythonanywhere_setup.sh

set -euo pipefail

PROJECT_NAME="site-pie_angola"
PROJECT_DIR="$HOME/$PROJECT_NAME"
VENV_DIR="$HOME/.virtualenvs/pieangola"
PYTHON_VERSION="3.13"
REPO_URL="https://github.com/RogerioChimuco/site-pie_angola.git"

echo ">>> 1. Clone do repositório"
if [ ! -d "$PROJECT_DIR" ]; then
    git clone "$REPO_URL" "$PROJECT_DIR"
else
    echo "    Já existe — fazendo pull..."
    cd "$PROJECT_DIR"
    git pull origin main
fi

echo ">>> 2. Criar virtualenv (Python $PYTHON_VERSION)"
if [ ! -d "$VENV_DIR" ]; then
    /usr/bin/python$PYTHON_VERSION -m venv "$VENV_DIR"
fi
# shellcheck disable=SC1091
source "$VENV_DIR/bin/activate"

echo ">>> 3. Instalar dependências"
cd "$PROJECT_DIR"
pip install --upgrade pip
pip install -r requirements.txt

echo ">>> 4. Migrações da base de dados"
export DJANGO_DEBUG=False
export DJANGO_ALLOWED_HOSTS="rochimuc.pythonanywhere.com,.pythonanywhere.com"
export DJANGO_DB_PATH="$PROJECT_DIR/db.sqlite3"
python manage.py migrate --noinput

echo ">>> 5. Collectstatic"
python manage.py collectstatic --noinput

echo ""
echo "============================================================"
echo "Setup concluído. Próximos passos no painel Web do PA:"
echo "  1. Web → Add new web app → Manual configuration → Python $PYTHON_VERSION"
echo "  2. Source code: $PROJECT_DIR"
echo "  3. Working directory: $PROJECT_DIR"
echo "  4. Virtualenv: $VENV_DIR"
echo "  5. WSGI file: copiar conteúdo de deploy/pythonanywhere_wsgi.py"
echo "  6. Static files mapping:"
echo "       URL: /static/   →   Directory: $PROJECT_DIR/staticfiles"
echo "  7. Environment variables (Web → Environment variables):"
echo "       DJANGO_SECRET_KEY = <gerar com: python -c 'import secrets;print(secrets.token_urlsafe(64))'>"
echo "  8. Reload da web app"
echo "============================================================"
