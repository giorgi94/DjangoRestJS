import os
import datetime as dt
from django.apps import apps
from django.conf import settings
# from . import token


def get_hash(name):
    HASH = ""
    if not settings.CONFIG.localhost:
        path = "{0}/build/hash/{1}-hash.txt".format(
            settings.BASE_DIR, name)

        if os.path.isfile(path):
            with open(path, 'r') as r:
                HASH = '-' + r.read().strip()
    return HASH


def handle(request):

    context = {
        'HASH': {
            'HASH_JS': get_hash('webpack'),
            'HASH_CSS': get_hash('gulp'),
        },
    }

    return context
