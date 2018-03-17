from django import forms
from django.core import exceptions
from django.db import models
import json


class JsonField(models.TextField):
    description = "JSON Field"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def from_db_value(self, value, expression, connection):
        try:
            if value is None:
                return {}
            return json.loads(value)
        except:
            return {}

    def get_prep_value(self, value):
        try:
            if value is None:
                return "{}"
            return json.dumps(value, ensure_ascii=False)
        except:
            return "{}"
