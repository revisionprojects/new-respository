"""
Django settings for my_django_project project.

Generated by 'django-admin startproject' using Django 3.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path,os
import django_heroku
import psycopg2
import dj_database_url

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'o7m6r49i+_^4b#eb5z7wipj9+s9gm(ao&po5hqcgzv*tie0^4z'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['0.0.0.0', 'localhost', '127.0.0.1', 'https://revision-projects.herokuapp.com/']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'Stock'
    'whitenoise.runserver_nostatic'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
ROOT_URLCONF = 'my_django_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'my_django_project.wsgi.application'


# Database
bashCommand = “heroku config:get DATABASE_URL -a app_name” #Use your app_name

output = subprocess.check_output([‘bash’,’-c’, bashCommand]).decode(“utf-8”) # executing the bash command and converting byte to string

DATABASES[‘default’] = dj_database_url.config(default=output,conn_max_age=600, ssl_require=True) #making connection to heroku DB without having to set DATABASE_URL env variable
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

#DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
#}


#db_from_env = dj_database_url.config(conn_max_age=500)
#DATABASES['default'].update(db_from_env)
#DATABASE_URL = os.environ['postgres://wlxvjqcfgjjjfp:f455971a1045b90ba66e67ae66af7163c667eee5e52b6da67b52cf9b32d4230f@ec2-54-156-60-12.compute-1.amazonaws.com:5432/de3u5bvtb0u0a2']

#conn = psycopg2.connect(DATABASE_URL, sslmode='require')

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'
#location where django collect all static files
STATIC_ROOT = os.path.join(BASE_DIR,'static')
# location where you will store your static files
STATICFILES_DIRS = [os.path.join(BASE_DIR,'project_name/static')
]
MEDIA_ROOT = os.path.join(BASE_DIR,'media')
MEDIA_URL = '/media/'

DATABASES['default'] = dj_database_url.config(conn_max_age=600, ssl_require=True)

django_heroku.settings(locals())
