from django import forms
from django.core import exceptions
from django.db import models
import json
from .mediaPIL import ImgField


class ImagePILField(models.TextField):
    description = "Image PIL Field"

    def __init__(self, default_path=None, default_point=(50, 50),
                 upload_to=".", *args, **kwargs):
        self.default_path = default_path
        self.default_point = default_point
        self.upload_to = upload_to
        super().__init__(*args, **kwargs)

    def from_db_value(self, value, expression, connection):
        if value is None:
            return value
        return json.loads(value)
        # return ImgField(value)

    def get_prep_value(self, value):
        return json.dumps(value, ensure_ascii=False)


"""
from apps.blog.models import Blog
blog = Blog.objects.all()[0]
blog.image
"""
