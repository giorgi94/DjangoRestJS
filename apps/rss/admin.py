from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from django.contrib import admin
from .models import RSSCollector, JSONStorage


@admin.register(RSSCollector)
class RSSCollectorAdmin(admin.ModelAdmin):
    pass


@admin.register(JSONStorage)
class JSONStorageAdmin(admin.ModelAdmin):
    pass
