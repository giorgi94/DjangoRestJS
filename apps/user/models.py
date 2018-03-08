from django.db import models
from .abstract_models import AbstractUser
from django.utils.translation import ugettext_lazy as _

from django.db.models.signals import post_save
from django.dispatch import receiver


class User(AbstractUser):
    pass
