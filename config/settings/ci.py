from .base import *

# These settings should only be used for CI only
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
        "HOST": "postgres",
        "PORT": 5432,
    }
}

# Static files handling
STATIC_URL = "static/"
STATICFILES_DIRS = [
    BASE_DIR / "static",
]
