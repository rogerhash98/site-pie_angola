"""
WSGI config para deploy em PythonAnywhere.

Copia o conteúdo deste ficheiro para o WSGI configuration file no painel Web do
PythonAnywhere (substitui o placeholder gerado automaticamente).

Caminho típico no PA:
    /var/www/rochimuc_pythonanywhere_com_wsgi.py
"""

import os
import sys

PROJECT_DIR = '/home/rochimuc/site-pie_angola'
if PROJECT_DIR not in sys.path:
    sys.path.insert(0, PROJECT_DIR)

# --- Variáveis de ambiente de produção ---
os.environ['DJANGO_DEBUG'] = 'False'
os.environ['DJANGO_ALLOWED_HOSTS'] = (
    'rochimuc.pythonanywhere.com,.pythonanywhere.com'
)
os.environ['DJANGO_CSRF_TRUSTED_ORIGINS'] = (
    'https://rochimuc.pythonanywhere.com,https://*.pythonanywhere.com'
)
os.environ['DJANGO_DB_PATH'] = f'{PROJECT_DIR}/db.sqlite3'
os.environ['DJANGO_STATICFILES_BACKEND'] = (
    'django.contrib.staticfiles.storage.StaticFilesStorage'
)

# IMPORTANTE: define DJANGO_SECRET_KEY no painel Web → Environment variables
# (NUNCA commitar a secret key real no código)
# Exemplo de geração local:
#   python -c "import secrets; print(secrets.token_urlsafe(64))"

os.environ['DJANGO_SETTINGS_MODULE'] = 'app.settings'

from django.core.wsgi import get_wsgi_application  # noqa: E402

application = get_wsgi_application()
