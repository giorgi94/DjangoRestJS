import os


DEBUG = True
DEBUG_TOOLS = True

CONFIG = {
    'localhost': True,
    'livereload': False
}

SITE_ID = 1

SECRET_KEY = '+3=!ljmsououh8&n3wykum$!+ch19bb6n=jzlxe==exig71to2'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(
            os.path.dirname(os.path.abspath(__file__)), '../../db.sqlite3'),
    }
}
