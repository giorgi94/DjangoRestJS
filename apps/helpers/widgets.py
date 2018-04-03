import os
import json
from xml.etree import ElementTree as xmltree
from django.conf import settings
from django.contrib.admin.widgets import AdminTextareaWidget


class XMLWidget(AdminTextareaWidget):

    def format_value(self, value):
        if type(value) == str:
            return value
        return xmltree.tostring(value, encoding='utf8', method='xml').decode()


class JSONWidget(AdminTextareaWidget):

    def format_value(self, value):
        if type(value) == str:
            return value
        return json.dumps(value, indent=4, ensure_ascii=False, sort_keys=True)
