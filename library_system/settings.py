from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.environ.get("SECRET_KEY", "unsafe-secret")

DEBUG = False

ALLOWED_HOSTS = ['*', 'my-project-5fi1.onrender.com']  # Backend URL for Render

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'library',
    'rest_framework',
    'rest_framework.authtoken',
    'corsheaders',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # muhimu kwa static
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# 🔥 CORS FIX
CORS_ALLOWED_ORIGINS = [
    "https://library-frontend-orpin.vercel.app",
    "https://library_system-api.onrender.com",
]
CORS_ALLOW_CREDENTIALS = True
CORS_ALLOW_ALL_ORIGINS = False

# Required when CORS_ALLOW_CREDENTIALS = True
CSRF_TRUSTED_ORIGINS = [
    "https://library-frontend-orpin.vercel.app",
    "https://library_system-api.onrender.com",
]

# Additional CORS settings for preflight requests
CORS_EXPOSE_HEADERS = ['Content-Type', 'Authorization']
CORS_ALLOW_METHODS = ['DELETE', 'GET', 'OPTIONS', 'PATCH', 'POST', 'PUT']
CORS_ALLOW_HEADERS = ['accept', 'accept-encoding', 'authorization', 'content-type', 'origin', 'user-agent', 'x-csrftoken', 'x-requested-with']

ROOT_URLCONF = 'library_system.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'library_system.wsgi.application'


import dj_database_url

DATABASES = {
    'default': dj_database_url.config(
        default='postgresql://library_db_qy0q_user:3t8TgcG7kgVmjq8v0vEwiu9umXHGurd8@dpg-d6gntgbuibrs739ge9sg-a.oregon-postgres.render.com:5432/library_db_qy0q'
    )
}


AUTH_PASSWORD_VALIDATORS = []

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# 🔥 STATIC CONFIG FOR RENDER
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'

# 🔥 MEDIA CONFIG
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# REST Framework
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny',
    ],
}
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"