from django import forms
from django.core import exceptions
from django.db import models
import json
from .mediaPIL import MediaPIL
from .widgets import ImagePILWidget


class ImagePILField(models.TextField):
    description = "Image PIL Field"

    def __init__(self, pathway="", point=(50, 50), quality=90,
                 upload_to=".", *args, **kwargs):

        if pathway is None:
            pathway = ""

        self.default_kwargs = {
            'pathway': pathway,
            'point': point,
            'quality': quality,
        }
        kwargs['default'] = json.dumps(
            self.default_kwargs, ensure_ascii=False)
        super().__init__(*args, **kwargs)

    def from_db_value(self, value, expression, connection):
        try:
            if value is None:
                return MediaPIL()
            kwargs = json.loads(value)
            return MediaPIL(**kwargs)
        except:
            return MediaPIL(**self.default_kwargs)

    def value_to_string(self, obj):
        value = self._get_val_from_obj(obj)
        return value

    def clean(self, value, model_instance):
        value = json.loads(value)
        return MediaPIL(**value)

    def get_prep_value(self, value):
        if type(value) != MediaPIL:
            value = MediaPIL(**self.default_kwargs)
        return value.to_str()

    def formfield(self, **kwargs):
        kwargs['widget'] = ImagePILWidget
        return super().formfield(**kwargs)


"""
from apps.blog.models import Blog
blog = Blog.objects.all()[0]
blog.image
"""
