import os
import datetime as dt
from django.apps import apps
from django.conf import settings
# from . import token


def get_HASH():
    HASH = "dev"
    if not settings.ON_LOCALHOST:
        try:
            with open(settings.BASE_DIR + '/context/hash', 'r') as r:
                HASH = r.read().strip()
        except:
            return 'prod'

    return HASH


def handle(request):

    context = {

    }

    return context
