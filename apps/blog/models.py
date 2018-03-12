import datetime as dt

from django.db import models
from django.utils import timezone as tz
from django.contrib.sites.models import Site
from django.utils import translation as lang
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from django.shortcuts import reverse
from django.utils.html import strip_tags
from django.utils.safestring import mark_safe

from apps.user.abstract_models import AbstractTime
from django.core.validators import MaxLengthValidator


def default_time_now():
    return dt.datetime.now().time()


def default_date_now():
    return dt.datetime.now().date()


class Blog(AbstractTime):
    user = models.ForeignKey('user.User', verbose_name=_('User'),
                             on_delete=models.SET_NULL, null=True)

    title = models.CharField(verbose_name=_("title"), max_length=200, null=True)
    alias = models.CharField(verbose_name=_("alias"), max_length=250, null=True)

    abstract = models.TextField(_('Abstract'), blank=True, null=True,
                                validators=[MaxLengthValidator(400)])
    content = models.TextField(_('Content'), null=True)

    pub_date = models.DateField(_('Publish Date'), default=default_date_now)
    pub_time = models.TimeField(_('Publish Time'), default=default_time_now)

    is_pub = models.BooleanField(_('Publish'), default=True)

    @staticmethod
    def filter_blogs(**kwargs):
        return Blog.objects.filter(
            is_pub=True,
            # pub_date__lte=tz.now(),
            **kwargs
        )

    def get_absolute_url(self):
        return reverse('blog:blog', kwargs={
            'pk': self.pk,
            'alias': self.alias,
        })

    class Meta:
        ordering = ['-pub_date']
        verbose_name = _('Blog')
        verbose_name_plural = _('Blogs')


class Comment(AbstractTime):
    user = models.ForeignKey('user.User', verbose_name=_('User'),
                             on_delete=models.CASCADE, null=True)
    blog = models.ForeignKey('blog.Blog', verbose_name=_('Blog'),
                             on_delete=models.CASCADE, null=True)
    content = models.TextField(_('content'), null=True)

    def get_absolute_url(self):
        return reverse('blog:blog', kwargs={
            'pk': self.blog.pk,
            'alias': self.blog.alias,
        }) + '#comment-' + self.pk

    class Meta:
        ordering = ['-pk']
        verbose_name = _('Comment')
        verbose_name_plural = _('Comments')


from .receivers import *

post_save.connect(set_alias, sender=Blog)
