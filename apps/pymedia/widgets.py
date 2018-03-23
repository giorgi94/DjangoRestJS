import os
import json
from django.conf import settings
from django.forms import widgets
from apps.pymedia.mediaPIL import MediaPIL

MEDIA_URL = settings.MEDIA_URL


class ImagePILWidget(widgets.TextInput):
    template_name = 'pymedia/image_widget.html'

    def url(self, pathway):
        if pathway is None:
            return None
        return os.path.join(MEDIA_URL, pathway)

    def format_value(self, value):
        if type(value) == str:
            value = json.loads(value)
            value['url'] = self.url(value['pathway'])
            return value
        return value.to_value()

    def get_context(self, name, value, attrs):
        context = super().get_context(name, value, attrs)
        value = context['widget']['value']
        context['json'] = json.dumps(value, ensure_ascii=False)
        context['MEDIA_URL'] = MEDIA_URL
        return context

    class Media:
        css = {
            'all': ('pymedia/widget.css',)
        }
        js = ('pymedia/widget.js',)
