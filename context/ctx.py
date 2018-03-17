import os
import datetime as dt
from django.apps import apps
from django.conf import settings
# from . import token


def get_hash(name):
    HASH = ""
    if not settings.ON_LOCALHOST:
        try:
            with open(
                    settings.BASE_DIR + '/context/hash/'
                    + name + '-hash.txt', 'r') as r:
                HASH = '-' + r.read().strip()
        except:
            return HASH
    return HASH


def handle(request):

    context = {
        'HASH_JS': '',  # get_hash('webpack'),
        'HASH_CSS': '',  # get_hash('gulp'),
    }

    return context
