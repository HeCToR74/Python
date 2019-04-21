"""
Django settings for techinterview project.

Generated by 'django-admin startproject' using Django 2.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os

try:
    from config.local_settings import *
    HOST = 'localhost'
except ImportError:
    SECRET_KEY = os.getenv('DJANGO', None)
    DB_PASS = os.getenv('DB_PASS', None)
    DB_USER = os.getenv('DB_USER', None)
    DB_NAME = os.getenv('DB_NAME', None)
    # DB_PORT = os.getenv('DB_PORT', None)
    HOST = 'postgres'
    SEND_GRID_API_KEY = os.getenv('SEND_GRID_API_KEY', None)
    EMAIL_HOST = os.getenv('EMAIL_HOST', None)
    EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER', None)
    EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD', None)
    EMAIL_PORT = os.getenv('EMAIL_PORT', None)
    EMAIL_USE_TLS = os.getenv('EMAIL_USE_TLS', None)
    SUBJECT = os.getenv('SUBJECT', None)
    EMAIL_BACKEND = os.getenv('EMAIL_BACKEND', None)

# Static email for sending letters
DEFAULT_FROM_EMAIL = 'recruiter@mail.com'

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

SITE_URL = 'http://localhost:8000'

OLD_PASSWORD_FIELD_ENABLED = True

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'questions.apps.QuestionsConfig',
    'feedback.apps.FeedbackConfig',
    'departments.apps.DepartmentsConfig',
    'rest_framework',
    'rest_framework.authtoken',
    'interviews.apps.InterviewsConfig',
    'authorization.apps.AuthorizationConfig',
    'django_rest_passwordreset',
    'rest_auth',
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'rest_auth.registration',
    'django_seed',
]

SITE_ID = 1

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'techinterview.middleware.middleware.AuthCheckMiddleware'
]

ROOT_URLCONF = 'techinterview.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates')
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

WSGI_APPLICATION = 'techinterview.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': DB_NAME,
        'USER': DB_USER,
        'PASSWORD': DB_PASS,
        'HOST': HOST,
        'PORT': '5432',
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static'),]

SESSION_COOKIE_HTTPONLY = False

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.AllowAny',
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.TokenAuthentication',
        'authorization.backend.CandidateAuthBackend'
    ),
}

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'authorization.backend.CandidateAuthBackend'
]