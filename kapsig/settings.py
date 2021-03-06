"""
Django settings for kapsig project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import ConfigParser
import dj_database_url
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

config = ConfigParser.ConfigParser()
config.read("config.ini")


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config.get('SecretKey', 'SecretKey')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = ['ksda.herokuapp.com']


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'datetimewidget',
    'phonenumber_field',
    'ksda'
)

LOGIN_URL = '/ksda/login'

LOGIN_REDIRECT_URL = '/ksda/'

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'kapsig.urls'

WSGI_APPLICATION = 'kapsig.wsgi.application'


PROJECT_ROOT = os.path.realpath(os.path.dirname(__file__)) + '/'

# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases
DATABASES = {}

db_from_env = dj_database_url.config(conn_max_age=500)
PRODUCTION = True #Set as True if in production
if(PRODUCTION):
    DATABASES['default'] = db_from_env
else:
    DATABASES['default'] = {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }



# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/New_York'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(PROJECT_ROOT, 'staticfiles')
FILE_UPLOAD_MAX_MEMORY_SIZE = 2500000


# Email Stuff

EMAIL_HOST = config.get('Email', 'Host')
EMAIL_PORT = config.get('Email', 'Port')
EMAIL_HOST_USER = config.get('Email', 'User')
EMAIL_HOST_PASSWORD = config.get('Email', 'Password')
EMAIL_USE_TLS = True
