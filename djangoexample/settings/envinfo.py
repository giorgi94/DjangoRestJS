import os


DEBUG = True
DEBUG_TOOLS = True

CONFIG = {
    'localhost': True,
    'livereload': False
}

SITE_ID = 1

SECRET_KEY = 'my_secret_key'

TOKEN_SECRET_KEY = 'my_secret_key_token'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(
            os.path.dirname(os.path.abspath(__file__)), '../../db.sqlite3'),
    }
}
