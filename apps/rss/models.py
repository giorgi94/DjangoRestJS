from django.utils.translation import ugettext_lazy as _
from django.db import models
from django.db.models import Q
from django.conf import settings
from django.shortcuts import reverse
from apps.helpers.fields import XMLField, JsonField


class RSSCollector(models.Model):
    name = models.CharField(_("სახელი"), max_length=128, blank=True)
    link = models.URLField(_("ლინკი"), max_length=128)

    xml_field = XMLField("XML", blank=True, null=True)

    def __str__(self):
        if self.name:
            return self.name
        return self.link

    class Meta:
        verbose_name = _('RSS კოლეკტორი')
        verbose_name_plural = _('RSS კოლეკტორები')


class JSONStorage(models.Model):
    data = JsonField("JSON", blank=True, null=True)
