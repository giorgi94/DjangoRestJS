from django.db import models
from django.contrib.sites.models import Site
from django.utils import translation as lang
from django.utils.translation import ugettext_lazy as _

from django.conf import settings
from django.shortcuts import reverse
from django.utils.html import strip_tags
from django.utils.safestring import mark_safe

from apps.user.abstract_models import AbstractTime
from django.core.validators import MaxLengthValidator


class Blog(AbstractTime):

    title = models.CharField(verbose_name=_("title"), max_length=200, null=True)
    alias = models.CharField(verbose_name=_("alias"), max_length=250, null=True)

    abstract = models.TextField(_('Abstract'), blank=True, null=True,
                                validators=[MaxLengthValidator(400)])
    content = models.TextField(_('Content'), null=True)

    class Meta:
        verbose_name = _('Blog')
        verbose_name_plural = _('Blogs')


from .receivers import *

post_save.connect(save_blog, sender=Blog)
