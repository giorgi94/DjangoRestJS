from django.db import models

# Create your models here.


class Person(models.Model):

    name = models.CharField('Name', max_length=50, null=True)