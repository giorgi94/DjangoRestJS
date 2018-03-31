from django.utils import timezone as tz
from django.utils import translation
from django.conf import settings

import jinja2
import json


def environment(**options):
    env = jinja2.Environment(**options)
    env.install_gettext_translations(translation)

    env.globals.update({
        'settings': settings,
        'tz': tz,
        'len': len,
        'str': str,
    })

    return env


def dump(instance, islist=False):
    try:
        return json.dumps(instance, ensure_ascii=False)
    except:
        return 'undefined'


jinja2.filters.FILTERS['dump'] = dump
