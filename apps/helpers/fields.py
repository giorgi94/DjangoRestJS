import json
from xml.etree import ElementTree as xmltree

from django import forms
from django.core import exceptions
from django.db.models import TextField

from .widgets import XMLWidget, JSONWidget


class JsonField(TextField):
    description = "JSON Field"

    def from_db_value(self, value, expression, connection):
        try:
            if value is None:
                return {}
            value = json.loads(value)
            if type(value) == str:
                value = json.loads(value)
            return value
        except:
            return {}

    def get_prep_value(self, value):
        try:
            if value is None:
                return "{}"
            return json.dumps(value, ensure_ascii=False)
        except:
            return "{}"

    def formfield(self, **kwargs):
        kwargs['widget'] = JSONWidget
        return super().formfield(**kwargs)


class XMLField(TextField):
    description = "XML Field"

    def from_db_value(self, value, expression, connection):
        try:
            if value is None:
                return None
            return xmltree.fromstring(value)
        except:
            return None

    def get_prep_value(self, value):
        try:
            if type(value) == str:
                return value
            return xmltree.tostring(value, encoding='utf8', method='xml').decode()
        except:
            return None

    def formfield(self, **kwargs):
        kwargs['widget'] = XMLWidget
        return super().formfield(**kwargs)
