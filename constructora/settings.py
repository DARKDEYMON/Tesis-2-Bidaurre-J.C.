"""
Django settings for constructora project.

Generated by 'django-admin startproject' using Django 1.10.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os
from django.core.urlresolvers import reverse_lazy

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'w3rdc@hpzl*v#@#s63z9rijpd4ds2rfoin=2v*e-nisp*retax'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_extensions',
    #importado de los diferentes modulos
    'django.contrib.postgres',
    'bootstrap3',
    'apps.almacenes',
    'apps.personal',
    'apps.seguimiento',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'constructora.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        #configuracion de la ubicacion de las plantillas
        'DIRS': [(os.path.join(BASE_DIR,"plantillas")),],
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

WSGI_APPLICATION = 'constructora.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        #configuracion de base de datos para postgresSql
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'constructora',
        'USER': 'postgres',
        'PASSWORD': '123456789',
        'PORT': '5432',
        'HOST': 'localhost',
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.10/topics/i18n/

#lenguage español latino
LANGUAGE_CODE = 'es-la'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_URL = '/static/'
#configuracion basica de rutas estaticas y rutas de carga de archibos
MEDIA_URL="/media/"
MEDIA_ROOT=os.path.join(BASE_DIR,"media")
STATICFILES_DIRS=(os.path.join(BASE_DIR,"static"),)

#configuracion de logeo de django para el redireccionamiento
LOGIN_REDIRECT_URL = reverse_lazy('personal:main')
LOGIN_URL = reverse_lazy('personal:login')
LOGOUT_URL = reverse_lazy('personal:logout')
LOGOUT_REDIRECT_URL = reverse_lazy('personal:login')

#DATE_FORMAT = "Y-m-d"
GRAPH_MODELS = {
  'all_applications': True,
  'group_models': True,
}