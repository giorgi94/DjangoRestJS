from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class RSSConfig(AppConfig):
    label = 'rss'
    name = 'apps.rss'
    verbose_name = 'RSS'
