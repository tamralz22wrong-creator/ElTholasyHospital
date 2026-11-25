"""
Django settings for the clinic management project.

القيم الحساسة وقيم البيئة تُقرأ من متغيرات البيئة
بدل كتابتها مباشرة في الكود.
"""

import os
from pathlib import Path

BASE_DIR = Path(**file**).resolve().parent.parent

# ---------------------------------------------------------------------------

# Helpers

# ---------------------------------------------------------------------------

def env_bool(name: str, default: bool = False) -> bool:
return (
os.environ.get(name, str(default))
.strip()
.lower()
in {"1", "true", "yes", "on"}
)

def env_list(name: str, default: str = "") -> list[str]:
return [
item.strip()
for item in os.environ.get(name, default).split(",")
if item.strip()
]

# ---------------------------------------------------------------------------

# Core

# ---------------------------------------------------------------------------

DEBUG = env_bool("DJANGO_DEBUG", True)

SECRET_KEY = os.environ.get("DJANGO_SECRET_KEY")

if not SECRET_KEY:
if DEBUG:
SECRET_KEY = "dev-only-insecure-key-change-me"
else:
raise RuntimeError(
"DJANGO_SECRET_KEY must be set when DEBUG is False."
)

ALLOWED_HOSTS = env_list(
"DJANGO_ALLOWED_HOSTS",
"localhost,127.0.0.1" if DEBUG else "",
)

# ---------------------------------------------------------------------------

# Applications

# ---------------------------------------------------------------------------

DJANGO_APPS = [
"django.contrib.admin",
"django.contrib.auth",
"django.contrib.contenttypes",
"django.contrib.sessions",
"django.contrib.messages",
"django.contrib.staticfiles",
]

THIRD_PARTY_APPS = [
"rest_framework",
"corsheaders",
]

LOCAL_APPS = [
"accounts",
"clinics",
"services",
"doctors",
"patients",
"appointments",
]

INSTALLED_APPS = (
DJANGO_APPS
+ THIRD_PARTY_APPS
+ LOCAL_APPS
)

# استخدام نموذج المستخدم المخصص

AUTH_USER_MODEL = "accounts.User"

# ---------------------------------------------------------------------------

# Middleware

# ---------------------------------------------------------------------------

MIDDLEWARE = [
"django.middleware.security.SecurityMiddleware",
"corsheaders.middleware.CorsMiddleware",
"django.contrib.sessions.middleware.SessionMiddleware",
"django.middleware.common.CommonMiddleware",
"django.middleware.csrf.CsrfViewMiddleware",
"django.contrib.auth.middleware.AuthenticationMiddleware",
"django.contrib.messages.middleware.MessageMiddleware",
"django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "config.urls"

WSGI_APPLICATION = "config.wsgi.application"

# ---------------------------------------------------------------------------

# Templates

# ---------------------------------------------------------------------------

TEMPLATES = [
{
"BACKEND": "django.template.backends.django.DjangoTemplates",
"DIRS": [BASE_DIR / "templates"],
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

# ---------------------------------------------------------------------------

# Database - MySQL

# ---------------------------------------------------------------------------

DATABASES = {
"default": {
"ENGINE": "django.db.backends.mysql",
"NAME": os.environ.get("DB_NAME", "clinic_db"),
"USER": os.environ.get("DB_USER", "root"),
"PASSWORD": os.environ.get("DB_PASSWORD", ""),
"HOST": os.environ.get("DB_HOST", "127.0.0.1"),
"PORT": os.environ.get("DB_PORT", "3306"),
"CONN_MAX_AGE": int(
os.environ.get("DB_CONN_MAX_AGE", "60")
),
"OPTIONS": {
"charset": "utf8mb4",
"init_command": (
"SET sql_mode='STRICT_TRANS_TABLES'"
),
},
}
}

# ---------------------------------------------------------------------------

# Django REST Framework

# ---------------------------------------------------------------------------

REST_FRAMEWORK = {
"DEFAULT_PERMISSION_CLASSES": [
"rest_framework.permissions.IsAuthenticated",
],
"DEFAULT_AUTHENTICATION_CLASSES": [
"rest_framework.authentication.SessionAuthentication",
"rest_framework.authentication.BasicAuthentication",
],
"DEFAULT_PAGINATION_CLASS": (
"rest_framework.pagination.PageNumberPagination"
),
"PAGE_SIZE": 20,
"DEFAULT_RENDERER_CLASSES": [
"rest_framework.renderers.JSONRenderer",
]
+ (
["rest_framework.renderers.BrowsableAPIRenderer"]
if DEBUG
else []
),
}

# ---------------------------------------------------------------------------

# CORS / CSRF

# ---------------------------------------------------------------------------

CORS_ALLOW_ALL_ORIGINS = DEBUG

CORS_ALLOWED_ORIGINS = env_list(
"DJANGO_CORS_ALLOWED_ORIGINS"
)

CSRF_TRUSTED_ORIGINS = env_list(
"DJANGO_CSRF_TRUSTED_ORIGINS"
)

# ---------------------------------------------------------------------------

# Password validation

# ---------------------------------------------------------------------------

_PV = "django.contrib.auth.password_validation."

AUTH_PASSWORD_VALIDATORS = [
{
"NAME": _PV + "UserAttributeSimilarityValidator",
},
{
"NAME": _PV + "MinimumLengthValidator",
"OPTIONS": {"min_length": 8},
},
{
"NAME": _PV + "CommonPasswordValidator",
},
{
"NAME": _PV + "NumericPasswordValidator",
},
]

# ---------------------------------------------------------------------------

# Internationalization

# ---------------------------------------------------------------------------

LANGUAGE_CODE = "ar"

TIME_ZONE = "Africa/Cairo"

USE_I18N = True

USE_TZ = True

LOCALE_PATHS = [
BASE_DIR / "locale",
]

# ---------------------------------------------------------------------------

# Static & Media Files

# ---------------------------------------------------------------------------

STATIC_URL = "static/"

STATIC_ROOT = BASE_DIR / "staticfiles"

MEDIA_URL = "media/"

MEDIA_ROOT = BASE_DIR / "media"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# ---------------------------------------------------------------------------

# Email

# ---------------------------------------------------------------------------

if DEBUG:
EMAIL_BACKEND = (
"django.core.mail.backends.console.EmailBackend"
)
else:
EMAIL_BACKEND = (
"django.core.mail.backends.smtp.EmailBackend"
)

```
EMAIL_HOST = os.environ.get("EMAIL_HOST", "")

EMAIL_PORT = int(
    os.environ.get("EMAIL_PORT", "587")
)

EMAIL_HOST_USER = os.environ.get(
    "EMAIL_HOST_USER", ""
)

EMAIL_HOST_PASSWORD = os.environ.get(
    "EMAIL_HOST_PASSWORD", ""
)

EMAIL_USE_TLS = env_bool(
    "EMAIL_USE_TLS", True
)
```

DEFAULT_FROM_EMAIL = os.environ.get(
"DEFAULT_FROM_EMAIL",
"[no-reply@example.com](mailto:no-reply@example.com)",
)

# ---------------------------------------------------------------------------

# Security - Production

# ---------------------------------------------------------------------------

if not DEBUG:
SECURE_SSL_REDIRECT = env_bool(
"DJANGO_SECURE_SSL_REDIRECT", True
)

```
SECURE_PROXY_SSL_HEADER = (
    "HTTP_X_FORWARDED_PROTO",
    "https",
)

SESSION_COOKIE_SECURE = True

CSRF_COOKIE_SECURE = True

SECURE_HSTS_SECONDS = 60 * 60 * 24 * 30

SECURE_HSTS_INCLUDE_SUBDOMAINS = True

SECURE_HSTS_PRELOAD = True

SECURE_CONTENT_TYPE_NOSNIFF = True

X_FRAME_OPTIONS = "DENY"
```

# ---------------------------------------------------------------------------

# Logging

# ---------------------------------------------------------------------------

LOGGING = {
"version": 1,
"disable_existing_loggers": False,
"formatters": {
"simple": {
"format": (
"[{levelname}] {asctime} "
"{name}: {message}"
),
"style": "{",
},
},
"handlers": {
"console": {
"class": "logging.StreamHandler",
"formatter": "simple",
},
},
"root": {
"handlers": ["console"],
"level": os.environ.get(
"DJANGO_LOG_LEVEL", "INFO"
),
},
}

