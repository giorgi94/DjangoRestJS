from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from django.contrib import admin
from .models import RSSCollector


@admin.register(RSSCollector)
class RSSCollectorAdmin(admin.ModelAdmin):
    pass

