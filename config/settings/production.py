from decouple import config

from .base import *

SECRET_KEY = config("DJANGO_SECRET_KEY")

DEBUG = config(DJANGO_DEBUG)

ALLOWED_HOSTS = config("ALLOWED_HOSTS").split(" ")
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": config("DBNAME"),
        "USER": config("DBUSER"),
        "PASSWORD": config("DBPASS"),
        "HOST": config("DBHOST"),
        "OPTIONS": {"sslmode": "require"},
    }
}

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = config("EMAIL_HOST")
EMAIL_PORT = 587
EMAIL_HOST_USER = config("EMAIL")
EMAIL_HOST_PASSWORD = config("EMAIL_PASSWORD")
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False

STATICFILES_STORAGE = 'core.azure_storage.AzureStaticStorage'

AZURE_ACCOUNT_NAME = config("AZURE_ACCOUNT_NAME")
AZURE_ACCOUNT_KEY = config("AZURE_ACCOUNT_KEY")
AZURE_CUSTOM_DOMAIN = f'{AZURE_ACCOUNT_NAME}.blob.core.windows.net'

STATIC_URL = f'https://{AZURE_CUSTOM_DOMAIN}/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
