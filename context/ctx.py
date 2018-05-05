import os
import datetime as dt
from django.apps import apps
from django.conf import settings


def get_hash(name):
    HASH = ""

    path = "{0}/context/hash/{1}-hash.txt".format(
        settings.BASE_DIR, name)

    if os.path.isfile(path):
        with open(path, 'r') as r:
            HASH = '-' + r.read().strip()
    return HASH


def handle(request):

    context = {}

    if not settings.CONFIG.get('localhost', False):
        context['HASH'] = {
            'HASH_JS': get_hash('webpack'),
            'HASH_CSS': get_hash('gulp'),
        }
    else:
        context['HASH'] = {
            'HASH_JS': '',
            'HASH_CSS': '',
        }

    return context
