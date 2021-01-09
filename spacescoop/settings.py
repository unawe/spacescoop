"""
Django settings for spacescoop project.

Generated by 'django-admin startproject' using Django 2.2.16.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os
import copy
import operator

import dj_database_url
from django_storage_url import dsn_configured_storage_class


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PARENT_DIR = os.path.dirname(BASE_DIR)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY', 'z2=$*^40@k+--2u@z8j8&c5!^3_o1-lc06#ih5^uboqtn(*1n0')


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get('DJANGO_DEBUG') == "True"

DIVIO_DOMAIN = os.environ.get('DOMAIN', '')

DIVIO_DOMAIN_ALIASES = [
    d.strip()
    for d in os.environ.get('DOMAIN_ALIASES', '').split(',')
    if d.strip()
]

ALLOWED_HOSTS = [DIVIO_DOMAIN] + DIVIO_DOMAIN_ALIASES
SITE_URL = 'https://www.spacescoop.org'


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'parler',
    'ckeditor',
    'taggit',
    'taggit_autosuggest',
    # 'compressor',

    'easy_thumbnails',

    'django_ext',
    'glossary',
    'institutions',
    'search',
    'smartpages',
    'spacescoops',
    'spacescoop'
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
    'django.middleware.locale.LocaleMiddleware'
]

ROOT_URLCONF = 'spacescoop.urls'

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
                'django.template.context_processors.i18n',
                # THUMBNAIL_ALIASES
                'django_ext.context_processors.thumbnail_aliases',
                # SITE_URL
                'django_ext.context_processors.site_url',
            ],
        },
    },
]

WSGI_APPLICATION = 'spacescoop.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DEFAULT_DATABASE_DSN = os.environ.get('DEFAULT_DATABASE_DSN', 'sqlite://:memory:')
DATABASES = {'default': dj_database_url.parse(DEFAULT_DATABASE_DSN)}


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

import django.conf.locale
django.conf.locale.LANG_INFO['gu'] = {
    'bidi': False,
    'code': 'gu',
    'name': 'Gurajati',
    'name_local': 'ગુજરાતી',
}
django.conf.locale.LANG_INFO['hi'] = {
    'bidi': False,
    'code': 'hi',
    'name': 'Hindi',
    'name_local': 'हिंदी',
}
django.conf.locale.LANG_INFO['mt'] = {
    'bidi': False,
    'code': 'mt',
    'name': 'Maltese',
    'name_local': 'Malti',
}
django.conf.locale.LANG_INFO['si'] = {
    'bidi': False,
    'code': 'si',
    'name': 'Sinhalese',
    'name_local': 'සිංහල',
}
django.conf.locale.LANG_INFO['tet'] = {
    'bidi': False,
    'code': 'tet',
    'name': 'Tetum',
    'name_local': 'tetun',
}
django.conf.locale.LANG_INFO['zh'] = {
    'fallback': ['zh-hans'],
}
django.conf.locale.LANG_INFO['quc'] = {
    'bidi': False,
    'code': 'quc',
    'name': 'K’iche’',
    'name_local': 'K’iche’',
}
django.conf.locale.LANG_INFO['tzj'] = {
    'bidi': False,
    'code': 'tzj',
    'name': 'Tz’utujil',
    'name_local': 'Tz’utujil',
}
django.conf.locale.LANG_INFO['ar'] = {
    'bidi': False,
    'code': 'ar',
    'name': 'Arabic',
    'name_local': 'العربيّة',
}
django.conf.locale.LANG_INFO['he'] = {
    'bidi': False,
    'code': 'he',
    'name': 'Hebrew',
    'name_local': 'עברית',
}

LANGUAGE_CODE = 'en'

LANGUAGES = (
    ('en', 'English'),
    ('nl', 'Dutch'),
    ('it', 'Italian'),
    ('de', 'German'),
    ('es', 'Spanish'),
    ('pl', 'Polish'),
    ('sq', 'Albanian'),
    ('ar', 'Arabic'),
    ('bn', 'Bengali'),
    ('bg', 'Bulgarian'),
    ('zh', 'Chinese'),
    ('cs', 'Czech'),
    ('da', 'Danish'),
    ('fa', 'Farsi'),
    ('fr', 'French'),
    ('el', 'Greek'),
    ('gu', 'Gujarati'),
    ('he', 'Hebrew'),
    ('hi', 'Hindi'),
    ('hu', 'Hungarian'),
    ('is', 'Icelandic'),
    ('id', 'Indonesian'),
    ('ja', 'Japanese'),
    ('quc', 'K’iche’'),
    ('ko', 'Korean'),
    ('mt', 'Maltese'),
    #('mam', 'Mam'),
    ('no', 'Norwegian'),
    ('pt', 'Portuguese'),
    ('ro', 'Romanian'),
    ('ru', 'Russian'),
    ('si', 'Sinhalese'),
    ('sl', 'Slovenian'),
    ('sw', 'Swahili'),
    ('ta', 'Tamil'),
    ('tet', 'Tetum'),
    ('tr', 'Turkish'),
    ('tzj', 'Tz’utujil'),
    ('uk', 'Ukrainian'),
    ('vi', 'Vietnamese'),
    ('cy', 'Welsh'),
)
PARLER_LANG_LIST = [{'code': l[0]} for l in LANGUAGES]
LANGUAGES = sorted(LANGUAGES, key=operator.itemgetter(0))

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


PARLER_LANGUAGES = {
    None: PARLER_LANG_LIST,
    'default': {
        'fallbacks': ['en'],
        'hide_untranslated': True,   # False is the default; let .active_translations() return fallbacks too.
    }
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

# STATICFILES_FINDERS = (
#     'django.contrib.staticfiles.finders.FileSystemFinder',
#     'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#     'compressor.finders.CompressorFinder',
# )

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

#  media
# DEFAULT_FILE_STORAGE is configured using DEFAULT_STORAGE_DSN

# read the setting value from the environment variable
DEFAULT_STORAGE_DSN = os.environ.get('DEFAULT_STORAGE_DSN')

# dsn_configured_storage_class() requires the name of the setting
DefaultStorageClass = dsn_configured_storage_class('DEFAULT_STORAGE_DSN')

# Django's DEFAULT_FILE_STORAGE requires the class name
DEFAULT_FILE_STORAGE = 'spacescoop.settings.DefaultStorageClass'

THUMBNAIL_DEFAULT_STORAGE  = DEFAULT_FILE_STORAGE

MEDIA_URL = 'media/'
MEDIA_ROOT = os.path.join('/data/media/')

# Thumbnails

THUMBNAIL_ALIASES = {
    '': {
        'avatar': {'size': (50, 50), 'crop': True},
        'original_news_source': {'size': (60, 60), 'crop': 'scale'},
        'article_feature': {'size': (880,410), 'crop': True},
        'article_cover': {'size': (680, 400), 'crop': True},
        'article_thumb': {'size': (320, 320), 'crop': True},
        'article_thumb_inline': {'size': (198, 200), 'crop': True},
    },
}

# CK editor
CKEDITOR_UPLOAD_PATH = 'upload/'
CKEDITOR_CONFIGS = {
    'smartpages': {
        'fillEmptyBlocks': False,
        'toolbar': 'Custom',
        'toolbar_Custom': [
            ['Source', ],
            ['Format', ],
            ['Bold', 'Italic', '-', 'Underline', 'Subscript', 'Superscript', '-', 'Undo', 'Redo', 'RemoveFormat', ],
            ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', ],
            ['Link', 'Unlink', ],
            ['Image', 'Table', 'SpecialChar', ],
            ['Maximize', 'ShowBlocks', ],
            ['BidiLtr', 'BidiRtl', ],
        ],
        'width': 845,
    },
    'default': {
        'fillEmptyBlocks': False,
        'toolbar': 'Custom',
        'toolbar_Custom': [
            ['Source', ],
            ['Bold', 'Italic', '-', 'Subscript', 'Superscript', '-', 'Undo', 'Redo', 'RemoveFormat', ],
            ['Link', 'Unlink', ],
            # ['Image', ],
            ['BidiLtr', 'BidiRtl', ],
        ],
    },
}
CKEDITOR_CONFIGS['small'] = copy.deepcopy(CKEDITOR_CONFIGS['default'])
CKEDITOR_CONFIGS['small']['height'] = 100

CKEDITOR_CONFIGS['spacescoop'] = copy.deepcopy(CKEDITOR_CONFIGS['default'])
CKEDITOR_CONFIGS['spacescoop']['extraPlugins'] = 'glossary'
CKEDITOR_CONFIGS['spacescoop']['contentsCss'] = ['%sckeditor/ckeditor/contents.css' % STATIC_URL, '%scss/ckeditor-content.css' % STATIC_URL]
CKEDITOR_CONFIGS['spacescoop']['toolbar_Custom'].insert(2, ['Glossary', ])

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format' : "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
            'datefmt' : "%d/%b/%Y %H:%M:%S"
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose',
        }
    },
    'loggers': {
        'django.request': {
            'handlers':['console'],
            'propagate': True,
            'level':'ERROR',
        },
        '': {
            'handlers': ['console'],
            'level': 'ERROR',
        },
    }
}
