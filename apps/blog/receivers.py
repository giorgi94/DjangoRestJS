from unidecode import unidecode
from django.template.defaultfilters import slugify

from django.dispatch import receiver
from django.db.models.signals import post_save, pre_delete


def set_alias(sender, instance, **kwargs):
    try:
        alias = slugify(unidecode(instance.title))
        if instance.alias != alias:
            instance.alias = alias
            instance.save()
    except Exception as ex:
        print('Exception:', ex)
