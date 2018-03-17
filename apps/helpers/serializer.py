import pytz
import datetime as dt
from random import shuffle
from math import floor, ceil
from itertools import groupby
from operator import itemgetter

from django.apps import apps
from django.db.models import Q
from django.conf import settings
from django.shortcuts import reverse
from django.utils import timezone as tz
from django.utils.translation import ugettext_lazy as _


Article = apps.get_model('articles', 'Article')

ARTICLE_IMAGE_SIZE = {
    'detail': '630x415',
    'big': '494x326',
    'slider': '544x358',
    'preview': '180x118',
    'tag': '248x162',
    'relate': '200x130',
    'right': '186x122',
}


def localize(publish):
    try:
        if publish.year >= 2018:
            return publish.strftime('%H:%M / %d-%m-%Y')
        return pytz.utc.localize(publish).astimezone(
            tz=pytz.timezone("Asia/Tbilisi")).strftime('%H:%M / %d-%m-%Y')
    except:
        return '00:00 / 00-00-0000'


OLDEST_DATE_LIMIT = tz.now() - tz.timedelta(days=500)


def articlePreviewSerializer(article, prefix='', size="preview", method="cover"):

    def get_size():
        return ARTICLE_IMAGE_SIZE.get(size, size)

    def get_image():
        point = article.get('%simage_point' % prefix)
        if not point is None:
            point = eval(point)
        return get_thumbnail(article.get('%simage' % prefix), get_size(), method, point)

    def get_publish_up():
        try:
            date = article.get('%spublish_up' % prefix)
            return localize(date)
        except:
            return "00:00 / 00-00-0000"

    def get_link():
        return reverse('articles:article', kwargs={
            'article_pk': article.get('%spk' % prefix),
            'article_alias': article.get('%salias' % prefix)
        })

    return {
        "title": article.get('%stitle' % prefix),
        "introtext": article.get('%sintrotext' % prefix, None),
        "publish_up": get_publish_up(),
        "image": get_image(),
        "link": get_link()
    }
