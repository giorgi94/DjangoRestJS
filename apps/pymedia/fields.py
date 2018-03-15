from django import forms
from django.core import exceptions
from django.db import models
import json
from .mediaPIL import MediaPIL


class ImagePILField(models.TextField):
    description = "Image PIL Field"

    def __init__(self, url=None, point=(50, 50), quality=90,
                 upload_to=".", *args, **kwargs):
        self.url = url
        self.point = point
        self.quality = quality
        self.upload_to = upload_to
        super().__init__(*args, **kwargs)

    def from_db_value(self, value, expression, connection):
        try:
            kwargs = json.loads(value)
            return MediaPIL(**kwargs)
        except:
            return None

    def get_prep_value(self, value):

        if not type(value) == dict:
            value = {}

        kwargs = {
            'url': self.url,
            'point': self.point,
            'quality': self.quality,
        }

        return json.dumps({**kwargs, **value}, ensure_ascii=False)


"""
from apps.blog.models import Blog
blog = Blog.objects.all()[0]
blog.image
"""
