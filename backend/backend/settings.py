"""
Django settings for backend project.

Generated by 'django-admin startproject' using Django 4.0.5.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

import os
from pathlib import Path
from dotenv import load_dotenv
from distutils.util import strtobool

load_dotenv()

from dotenv import load_dotenv

load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = bool(strtobool(os.getenv("DEBUG", "True")))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "*" if DEBUG else os.getenv("SECRET_KEY")

ALLOWED_HOSTS = ["127.0.0.1", "localhost", "0.0.0.0"]
if DEBUG:
    ALLOWED_HOSTS.append("*")

# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "djoser",
    "import_export",
    "rest_framework",
    "knox",
    "drf_yasg",
    "organization",
    "project",
    "video",
    "transcript",
    "translation",
    "users",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# Email Settings
EMAIL_BACKEND = "django_smtp_ssl.SSLEmailBackend"
EMAIL_HOST = os.getenv("EMAIL_HOST")
EMAIL_PORT = 465
EMAIL_HOST_USER = ""
EMAIL_HOST_PASSWORD = ""
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = os.getenv("DEFAULT_FROM_EMAIL")

DOMAIN = "chitralekha.ai4bharat.org"
SITE_NAME = "chitralekha.ai4bharat.org"

DJOSER = {
    "PASSWORD_RESET_CONFIRM_URL": "forget-password/confirm/{uid}/{token}",
    "USERNAME_RESET_CONFIRM_URL": "users/auth/users/username/reset/confirm/{uid}/{token}",
    "ACTIVATION_URL": "users/auth/users/activation/{uid}/{token}",
    "SEND_ACTIVATION_EMAIL": True,
    "SERIALIZERS": {},
}

ENABLE_CORS = bool(strtobool(os.getenv("ENABLE_CORS", "False")))

if ENABLE_CORS:
    INSTALLED_APPS.append("corsheaders")
    MIDDLEWARE.insert(0, "corsheaders.middleware.CorsMiddleware")

    CORS_ALLOW_ALL_ORIGINS = True
    CSRF_COOKIE_SECURE = False
    CORS_ORIGIN_ALLOW_ALL = True
    CORS_ALLOW_CREDENTIALS = True

    CSRF_TRUSTED_ORIGINS = [
        "http://localhost:*",  # for localhost (Developlemt)
    ]
    CUSTOM_CSRF_TRUSTED_ORIGINS = os.getenv("CORS_TRUSTED_ORIGINS", "")
    if CUSTOM_CSRF_TRUSTED_ORIGINS:
        CSRF_TRUSTED_ORIGINS.extend(CUSTOM_CSRF_TRUSTED_ORIGINS.split(","))


ROOT_URLCONF = "backend.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "backend.wsgi.application"

REST_FRAMEWORK = {
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.AllowAny",
    ],
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework.authentication.BasicAuthentication",
        "knox.auth.TokenAuthentication",
    ],
}

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": os.getenv("POSTGRES_DB_NAME"),
        "USER": os.getenv("POSTGRES_DB_USERNAME"),
        "PASSWORD": os.getenv("POSTGRES_DB_PASSWORD"),
        "HOST": os.getenv("POSTGRES_DB_HOST"),
        "PORT": os.getenv("POSTGRES_DB_PORT"),
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

# Add Knox settings to Django settings
REST_KNOX = {
    "TOKEN_TTL": None,  # None means no expiration
}

# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = "static/"

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
AUTH_USER_MODEL = "users.User"
