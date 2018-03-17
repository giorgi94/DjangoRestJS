import os

DEBUG = True

DEBUG_TOOLS = False

CONFIG = {
    'localhost': True,
    'livereload': False
}


SITE_ID = 1
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


SECRET_KEY = '+3=!ljmsououh8&n3wykum$!+ch19bb6n=jzlxe==exig71to2'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


'''
# EMAIL CONFIGURATIONS
EMAIL_HOST=''
EMAIL_HOST_USER =''
EMAIL_HOST_PASSWORD=''
EMAIL_PORT=587
EMAIL_USE_TLS=True
'''
