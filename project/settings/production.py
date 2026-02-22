import os
import dj_database_url
from .base import *

DEBUG = False

# Дозволити доступ з доменів Render (або заданих через ENV)
ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', 'chaykovska.com,.onrender.com').split(',')

# Використання DATABASE_URL, якщо змінна присутня (наприклад, на Render)
if 'DATABASE_URL' in os.environ:
    DATABASES = {
        'default': dj_database_url.config(
            conn_max_age=600,
            conn_health_checks=True,
            ssl_require=True,
        )
    }
else:
    # Поточна локальна/резервна конфігурація
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': os.environ.get('DB_NAME', 'chaykovska'),
            'USER': os.environ.get('DB_USER', 'postgres'),
            'PASSWORD': os.environ.get('DB_PASSWORD'),
            'HOST': os.environ.get('DB_HOST'),
            'PORT': os.environ.get('DB_PORT', '5432'),
        }
    }

# Security
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
SECURE_SSL_REDIRECT = True
SECURE_HSTS_SECONDS = 31536000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True

CSRF_TRUSTED_ORIGINS = os.environ.get('CSRF_TRUSTED_ORIGINS', 'https://*.onrender.com').split(',')
