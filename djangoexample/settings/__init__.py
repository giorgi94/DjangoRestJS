import os
from .envinfo import *


BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.dirname(
            os.path.abspath(__file__))))

ALLOWED_HOSTS = ['*']


SITE_NAME = "Django Example"
PROJECT_NAME = 'djangoexample'

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sitemaps',
    'django.contrib.sites',

    # Packages
    # 'adminsortable2',
    'rest_framework',
    'django_jinja',
    'graphene_django',
    'haystack',

    # Custom apps
    'apps.pymedia',
    'apps.user',
    'apps.blog',

    'apps.search',
]


AUTH_USER_MODEL = 'user.User'
LOGIN_URL = '/'

ROOT_URLCONF = '%s.urls' % PROJECT_NAME

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

if DEBUG and DEBUG_TOOLS:
    INSTALLED_APPS += [
        'debug_toolbar',
    ]

    MIDDLEWARE += [
        'debug_toolbar.middleware.DebugToolbarMiddleware',
    ]

    INTERNAL_IPS = [
        '127.0.0.1',
    ]


# Caches

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': os.path.join(BASE_DIR, 'cache/apps'),
    },
    'sessions': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': os.path.join(BASE_DIR, 'cache/sessions'),
    },
    # 'redis': {
    #     "BACKEND": "django_redis.cache.RedisCache",
    #     "LOCATION": "redis://127.0.0.1:6379/0",
    #     "OPTIONS": {
    #         "CLIENT_CLASS": "django_redis.client.DefaultClient",
    #         "COMPRESSOR": "django_redis.compressors.zlib.ZlibCompressor",
    #         "SOCKET_CONNECT_TIMEOUT": 5,  # in seconds
    #         "SOCKET_TIMEOUT": 5,  # in seconds
    #         "IGNORE_EXCEPTIONS": True,
    #     }
    # }
}


# Session

SESSION_ENGINE = "django.contrib.sessions.backends.cache"
SESSION_CACHE_ALIAS = 'sessions'


# Search

WHOOSH_INDEX = os.path.join(BASE_DIR, 'whoosh_index')

HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.whoosh_backend.WhooshEngine',
        'PATH': WHOOSH_INDEX,
        'POST_LIMIT': 128 * 1024 * 1024,
        'INCLUDE_SPELLING': True,
        'BATCH_SIZE': 100,
    },
}

HAYSTACK_SIGNAL_PROCESSOR = 'haystack.signals.RealtimeSignalProcessor'
# HAYSTACK_LIMIT_TO_REGISTERED_MODELS = False

# Logging

# from .bin.mail import *

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        },
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    'formatters': {
        'django.server': {
            '()': 'django.utils.log.ServerFormatter',
            'format': '[%(server_time)s] %(message)s',
        }
    },
    'handlers': {
        'console': {
            'level': 'INFO',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
        },
        'django.server': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'django.server',
        },
        'mail_server_errors': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': '%s.settings.logging.ServerErrorHandler' % PROJECT_NAME,
        }
    },
    'loggers': {
        'django': {
            'handlers': ['console', 'mail_server_errors'],
            'level': 'INFO',
        },
        'django.server': {
            'handlers': ['django.server'],
            'level': 'INFO',
            'propagate': False,
        },
    }
}


# Rest Framework

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.SessionAuthentication',
        # 'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticatedOrReadOnly',
    ),
}

if CONFIG.get('localhost'):
    REST_FRAMEWORK['DEFAULT_RENDERER_CLASSES'] = (
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
    )
else:
    REST_FRAMEWORK['DEFAULT_RENDERER_CLASSES'] = (
        'rest_framework.renderers.JSONRenderer',
    )


# GraphQL

GRAPHENE = {
    'SCHEMA': 'apps.graphQL.schema.schema'
}

# Templates

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates/django')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'context.ctx.handle',
            ],
        },
    },
    {
        'BACKEND': 'django.template.backends.jinja2.Jinja2',
        'DIRS': [os.path.join(BASE_DIR, 'templates/jinja2'), ],
        'APP_DIRS': True,
        'OPTIONS': {
            'environment': '%s.settings.jinja2.environment' % PROJECT_NAME,
            'extensions': [
                "jinja2.ext.do",
                "jinja2.ext.loopcontrols",
                "jinja2.ext.with_",
                "jinja2.ext.i18n",
                "jinja2.ext.autoescape",

                "django_jinja.builtins.extensions.CsrfExtension",
                "django_jinja.builtins.extensions.CacheExtension",
                "django_jinja.builtins.extensions.TimezoneExtension",
                "django_jinja.builtins.extensions.UrlsExtension",
                "django_jinja.builtins.extensions.StaticFilesExtension",
                "django_jinja.builtins.extensions.DjangoFiltersExtension",

                "%s.settings.jinja2htmlcompress.HTMLCompress" % PROJECT_NAME,
            ],
            'context_processors': [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "django.template.context_processors.i18n",

                'context.ctx.handle',
            ],
        }
    },
]


WSGI_APPLICATION = '%s.wsgi.application' % PROJECT_NAME


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


# INTERNATIONALIZATION

from django.utils.translation import ugettext_lazy as _

LANGUAGE_CODE = 'en'

TIME_ZONE = 'Asia/Tbilisi'
USE_I18N = True
USE_L10N = True
USE_TZ = True


LOCALE_PATHS = [
    os.path.join(BASE_DIR, 'locale')
]

LANGUAGES = [
    ('ka', _('Georgian')),
    ('en', _('English')),
    ('ru', _('Russian')),
]


# STATIC FILES (CSS, JavaScript, Images)


MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR,  'media')
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'staticfiles'),
    os.path.join(BASE_DIR, 'assets'),
]

if os.path.isdir(os.path.join(BASE_DIR, 'dist')):
    STATICFILES_DIRS += [
        os.path.join(BASE_DIR, 'dist'),
    ]

if os.path.isdir(os.path.join(BASE_DIR, 'bower_components')):
    STATICFILES_DIRS += [
        os.path.join(BASE_DIR, 'bower_components'),
    ]
