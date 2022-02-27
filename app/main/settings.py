"""
Django settings for main project.

Generated by 'django-admin startproject' using Django 2.0.9.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os
import json

from pathlib import Path

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = Path(__file__).resolve().parent.parent

try:
    with open(os.path.join(BASE_DIR, 'config.json')) as config_file:
        config = json.load(config_file)
except IOError:
    config = {}

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY', 'development_key')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = bool(int(os.environ.get('DEBUG', 1)))
ADMINS = [('admin', os.environ.get('DJANGO_LOGGING_EMAIL'))]

ALLOWED_HOSTS = []
ALLOWED_HOSTS_ENV = os.environ.get('ALLOWED_HOSTS')
if ALLOWED_HOSTS_ENV:
    ALLOWED_HOSTS.extend(ALLOWED_HOSTS_ENV.split(','))
else:
    ALLOWED_HOSTS.append('*')

# For debug_toolbar
INTERNAL_IPS = ('127.0.0.1', '0.0.0.0', 'localhost',)

# Application definition
# https://medium.com/@zero_fighter/django-debug-toolbar-setup-2bf81736efe3

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.sites',
    'django.contrib.staticfiles',
    'django_userforeignkey',
    'django_select2',
    'rest_framework',
    'rnames_app',
    'simple_history',
    'debug_toolbar',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.orcid',
    'frontend.apps.FrontendConfig',
    'livereload'
]

LIVERELOAD_HOST="0.0.0.0"
LIVERELOAD_PORT="8002"

SITE_ID = 1

SOCIALACCOUNT_PROVIDERS = {
    'orcid': {
        'BASE_DOMAIN': 'orcid.org',
        'MEMBER_API': False,
        'APP': {
            'client_id': os.environ.get('ORCID_CLIENT_ID', config.get('ORCID_CLIENT_ID', '')),
            'secret': os.environ.get('ORCID_SECRET', config.get('ORCID_SECRET', '')),
            'key': '',
        }
    }
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django_userforeignkey.middleware.UserForeignKeyMiddleware',
    'simple_history.middleware.HistoryRequestMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'livereload.middleware.LiveReloadScript',
]

ROOT_URLCONF = 'main.urls'


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]

ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_CONFIRM_EMAIL_ON_GET = True
ACCOUNT_EMAIL_VERIFICATION = "mandatory"
ACCOUNT_SESSION_REMEMBER = True
ACCOUNT_LOGIN_ON_EMAIL_CONFIRMATION = True

WSGI_APPLICATION = 'main.wsgi.application'

REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        #        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ]
}

# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases
# https://stackoverflow.com/questions/19189813/setting-django-up-to-use-mysql
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': os.environ.get('DB_HOST', config.get('DB_HOST')),
        'NAME': os.environ.get('DB_NAME', config.get('DB_NAME')),
        'USER': os.environ.get('DB_USER', config.get('DB_USER')),
        'PASSWORD': os.environ.get('DB_PASSWORD', config.get('DB_PASS')),
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
            'charset': 'utf8mb4',
        },
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Europe/Helsinki'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.environ.get('STATIC_ROOT', os.path.join(BASE_DIR, 'static'))

# Redirect to home URL after login (Default redirects to /accounts/profile/)
LOGIN_REDIRECT_URL = '/'

# https://medium.com/@zero_fighter/django-debug-toolbar-setup-2bf81736efe3
DEBUG_TOOLBAR_PANELS = [
    'debug_toolbar.panels.versions.VersionsPanel',
    'debug_toolbar.panels.timer.TimerPanel',
    'debug_toolbar.panels.settings.SettingsPanel',
    'debug_toolbar.panels.headers.HeadersPanel',
    'debug_toolbar.panels.request.RequestPanel',
    'debug_toolbar.panels.sql.SQLPanel',
    'debug_toolbar.panels.staticfiles.StaticFilesPanel',
    'debug_toolbar.panels.templates.TemplatesPanel',
    'debug_toolbar.panels.cache.CachePanel',
    'debug_toolbar.panels.signals.SignalsPanel',
    'debug_toolbar.panels.logging.LoggingPanel',
    'debug_toolbar.panels.redirects.RedirectsPanel',
]

DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'

EMAIL_BACKEND = os.environ.get('EMAIL_BACKEND', config.get(
    'EMAIL_BACKEND', 'django.core.mail.backends.console.EmailBackend'))
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = os.environ.get('EMAIL_USER', config.get('EMAIL_USER'))
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_PASS', config.get('EMAIL_PASS'))
