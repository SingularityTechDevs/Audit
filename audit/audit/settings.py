from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-skr2!wj4s&bqd85pt=bf#b*d5%7&6d=0!$!i8rn4(^uxp&rbut'

DEBUG = False

ALLOWED_HOSTS = ['178.128.145.204','127.0.0.1','.vercel.app']

CORS_ORIGIN_ALLOW_ALL = True

INSTALLED_APPS = [
   'django.contrib.admin',
   'django.contrib.auth',
   'django.contrib.contenttypes',
   'django.contrib.sessions',
   'django.contrib.messages',
   'django.contrib.staticfiles',
   'fontawesome_5',
   'corsheaders',
   'core',
   'visitas',
]

MIDDLEWARE = [
   'django.middleware.security.SecurityMiddleware',
   'django.contrib.sessions.middleware.SessionMiddleware',
   'django.middleware.common.CommonMiddleware',
   'django.middleware.csrf.CsrfViewMiddleware',
   'django.contrib.auth.middleware.AuthenticationMiddleware',
   'django.contrib.messages.middleware.MessageMiddleware',
   'django.middleware.clickjacking.XFrameOptionsMiddleware',
   'corsheaders.middleware.CorsMiddleware',
]

ROOT_URLCONF = 'audit.urls'

TEMPLATES = [
   {
       'BACKEND': 'django.template.backends.django.DjangoTemplates',
       'DIRS': ['templates',
               os.path.join(BASE_DIR, "templates", "login"),
               os.path.join(BASE_DIR, "templates", "core"),
               os.path.join(BASE_DIR, "templates", "visitas"), 
               os.path.join(BASE_DIR, "templates", "pacientes"),
               os.path.join(BASE_DIR, "templates", "recetas"),
               os.path.join(BASE_DIR, "templates", "email"),
        ],
       'APP_DIRS': True,
       'OPTIONS': {
           'context_processors': [
               'django.template.context_processors.debug',
               'django.template.context_processors.request',
               'django.contrib.auth.context_processors.auth',
               'django.contrib.messages.context_processors.messages',
           ],
       },
   },
]

WSGI_APPLICATION = 'audit.wsgi.application'

AUTH_USER_MODEL = 'core.Usuario'

DATABASES = {
   'default': {
       'ENGINE': 'django.db.backends.sqlite3',
       'NAME': BASE_DIR / 'db.sqlite3',
   }
}

AUTH_PASSWORD_VALIDATORS = [
   {
       'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
   },
   {
       'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
   },
   {
       'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
   },
   {
       'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
   },
]

EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'ceo.singularity@singularity-tech.net'
EMAIL_HOST_PASSWORD = 'cvnb hvht rnfc ohef'
EMAIL_PORT = 587
DEFAULT_FROM_EMAIL = 'no-reply <ceo.singularity@singularity-tech.net>'
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = False

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = [
   BASE_DIR / "static",
]

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

LOGIN_URL = '/login/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'