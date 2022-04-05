"""
Django settings for cms project.

Generated by 'django-admin startproject' using Django 2.2.10.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import django_heroku
import os
import cloudinary
# NEW
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# OLD SETTINGS
# # Build paths inside the project like this: os.path.join(BASE_DIR, ...)
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')

TEMPLATES_DIR = BASE_DIR / 'templates'


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '-c_m6!nr-(hr5it9jg1ihj4s)^a)w+xi8xcxq&p*074hq0ln&4'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['127.0.0.1','postindianews.pythonanywhere.com','www.postindianews.com','postindianews.herokuapp.com']
CSRF_TRUSTED_ORIGINS=['https://www.postindianews.com','https://postindianews.com','127.0.0.1']

# Application definition
SITE_ID = 1

INSTALLED_APPS = [
    'whitenoise.runserver_nostatic',
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'blog',
    'account',
    'tinymce',
    'django.contrib.sites',
    'django.contrib.sitemaps',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django_session_timeout.middleware.SessionTimeoutMiddleware',
]

ROOT_URLCONF = 'cms.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATES_DIR],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'blog.context_processors.Categorys',
                'blog.context_processors.BlogPost',
            ],
        },
    },
]

WSGI_APPLICATION = 'cms.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases



DATABASES = {
'default': {
'ENGINE': 'django.db.backends.postgresql',
'NAME': 'd7s911cdhoo4dr',
'USER': 'ixhrhoiflhghxc',
'PASSWORD': 'b096f39c2ecfd94d8abb5ce3d87010cde6a4bc4f39c54df862a32ad959363f46',
'HOST': 'ec2-52-212-228-71.eu-west-1.compute.amazonaws.com',
'PORT':'5432',
}
}

#done

# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))


# STATIC_ROOT = os.path.join(PROJECT_DIR, 'static')
STATIC_ROOT = BASE_DIR / 'static'
STATIC_URL = '/static/'

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Media files
MEDIA_URL = '/media/'
# MEDIA_ROOT = os.path.join(BASE_DIR, "media")
MEDIA_ROOT = BASE_DIR / 'media'


# Login/Logout Redirect urls
LOGIN_REDIRECT_URL = '/blogs'
LOGOUT_REDIRECT_URL = '/blogs'

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

AUTH_USER_MODEL = 'account.MyUser'

# TINYMCE_JS_URL = os.path.join(MEDIA_URL, "tinymce/js/tinymce/tinymce.min.js")
# TINYMCE_JS_ROOT = os.path.join(MEDIA_ROOT, "tinymce")

TINYMCE_JS_URL = os.path.join(STATIC_URL, "tinymce/tinymce.min.js")
TINYMCE_JS_ROOT = os.path.join(STATIC_ROOT, "tinymce")


TINYMCE_DEFAULT_CONFIG = {
    "height": "400px",
    "width": "700px",
    "menubar": "file edit view insert format tools table help",
    "plugins": "advlist autolink lists link image charmap print preview anchor searchreplace visualblocks code "
    "fullscreen insertdatetime media table paste code help wordcount spellchecker",
    "toolbar": "undo redo | bold italic underline strikethrough | fontselect fontsizeselect formatselect | alignleft "
    "aligncenter alignright alignjustify | outdent indent |  numlist bullist checklist | forecolor "
    "backcolor casechange permanentpen formatpainter removeformat | pagebreak | charmap emoticons | "
    "fullscreen  preview save print | insertfile image media pageembed template link anchor codesample | "
    "a11ycheck ltr rtl | showcomments addcomment code",
    "custom_undo_redo_levels": 10,
    "language": "es_ES",  # To force a specific language instead of the Django current language.
}

ADMIN_SITE_HEADER = "Post India News"

SESSION_EXPIRE_SECONDS = 43200

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

cloudinary.config(
cloud_name='dtdr6woby',
api_key='227497839798671',
api_secret='RTZW4qlOeQKWa64zscB5yvztBL0',
secure=True,
)

django_heroku.settings(locals())