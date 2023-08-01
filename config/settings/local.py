from .base import *

# These settings should only be used for development only
# NOT SUITABLE FOR PRODUCTION

SECRET_KEY = "changemeinproduction"

DEBUG = True

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"


# Databases
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "postgres",
        "USER": "postgres",
        "PASSWORD": "postgres",
        "HOST": "db",
        "PORT": 5432,
    }
}

# Static files handling
STATIC_URL = "static/"
