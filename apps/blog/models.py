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
from apps.pymedia.fields import ImagePILField


def default_time_now():
    return dt.datetime.now().time()


def default_date_now():
    return dt.datetime.now().date()


class Category(models.Model):

    title = models.CharField(_('Title'), max_length=400, null=True, unique=True)
    alias = models.CharField(_('Alias'), max_length=400, null=True)

    description = models.TextField(_('Description'), blank=True, null=True)
    active = models.BooleanField(_('Active'), default=False, blank=True)

    def get_absolute_url(self):
        return reverse('blog:category', kwargs={'alias': self.alias})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')


class Tag(models.Model):
    name = models.CharField(_('Name'), max_length=35, null=True)

    def get_absolute_url(self):
        return reverse('blog:tag', kwargs={'name': self.name})

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Tag')
        verbose_name_plural = _('Tags')


class Blog(AbstractTime):
    user = models.ForeignKey('user.User', verbose_name=_('User'),
                             on_delete=models.SET_NULL, null=True)

    category = models.ForeignKey('blog.Category', verbose_name=_('Category'),
                                 on_delete=models.SET_NULL, null=True)

    tags = models.ManyToManyField('Tag', verbose_name=_('Tags'),
                                  blank=True, related_name='blogs')

    title = models.CharField(verbose_name=_("Title"), max_length=200, null=True)
    alias = models.CharField(verbose_name=_("Alias"), max_length=250, null=True)

    image = ImagePILField(verbose_name=_("image"), null=True)

    abstract = models.TextField(_('Abstract'), blank=True, null=True,
                                validators=[MaxLengthValidator(400)])
    content = models.TextField(_('Content'), null=True)

    pub_date = models.DateField(_('Publish Date'), default=default_date_now)
    pub_time = models.TimeField(_('Publish Time'), default=default_time_now)

    is_pub = models.BooleanField(_('Publish'), default=True)

    @property
    def attr(self):
        return "my attr"

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
post_save.connect(set_alias, sender=Category)
