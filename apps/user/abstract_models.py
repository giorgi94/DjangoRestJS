from django.db import models
from django.shortcuts import reverse
from django.utils import timezone as tz
from django.utils.translation import ugettext_lazy as _

from django.core.exceptions import ValidationError
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.models import PermissionsMixin

from django.core.mail import EmailMessage
from django.template.loader import render_to_string

import re
import random
from string import ascii_lowercase as al
from string import ascii_uppercase as uc
from string import digits as dg


def name_validation(name):
    if re.fullmatch(r'[^\W\d]+', name) is None:
        raise ValidationError(_('Field has unexpected character'))


class AbstractTime(models.Model):
    created = models.DateTimeField(_('Created'), auto_now_add=True, null=True)
    updated = models.DateTimeField(_('Updated'), auto_now=True, null=True)

    class Meta:
        abstract = True


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **kwargs):
        if not email:
            raise ValueError(_('email is requested'))

        if not kwargs.get('first_name'):
            raise ValueError(_('first name is requested'))

        if not kwargs.get('last_name'):
            raise ValueError(_('last name is requested'))

        account = self.model(
            email=self.normalize_email(email),
            first_name=kwargs.get('first_name'),
            last_name=kwargs.get('last_name')
        )
        account.set_password(password)
        account.save()
        return account

    def create_superuser(self, email, password, **kwargs):
        account = self.create_user(email, password, **kwargs)
        account.is_staff = True
        account.is_admin = True
        account.is_active = True
        account.is_superuser = True
        account.save()

        return account


class AbstractUser(AbstractBaseUser, PermissionsMixin, AbstractTime):
    email = models.EmailField(verbose_name=_("Email"), unique=True)

    first_name = models.CharField(verbose_name=_("First name"),
                                  max_length=40, validators=[name_validation])
    last_name = models.CharField(verbose_name=_("Last name"),
                                 max_length=40, validators=[name_validation])

    is_admin = models.BooleanField(_('admin'), default=False)
    is_staff = models.BooleanField(_('staff'), default=False)
    is_active = models.BooleanField(_('active'), default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def __str__(self):
        return self.email

    def make_superuser(self):
        self.is_admin = True
        self.is_staff = True
        self.is_active = True
        self.is_superuser = True
        self.save()

    def get_full_name(self):
        if self.first_name != '' and self.last_name != '':
            return ' '.join([self.first_name, self.last_name])
        return self.email

    def get_short_name(self):
        return self.first_name

    def send_mail(self, subject, template, context):
        try:
            body = render_to_string(template, context)
            msg = EmailMessage(
                subject,
                body,
                settings.EMAIL_HOST_USER,
                (self.email,)
            )
            msg.content_subtype = "html"
            msg.send()
        except Exception as ex:
            print('Email was not sent')
            print(ex)

    class Meta:
        abstract = True
        ordering = ['created']
        verbose_name = _('User')
        verbose_name_plural = _('Users')
