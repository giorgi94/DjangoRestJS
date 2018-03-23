from django.conf import settings
from django.utils.safestring import mark_safe
from django.forms import widgets
from apps.pymedia.mediaPIL import MediaPIL
import json

MEDIA_URL = settings.MEDIA_URL


class ImagePILWidget(widgets.TextInput):
    template_name = 'pymedia/image_widget.html'

    def url(self, pathway):
        if pathway is None:
            return None
        return os.path.join(MEDIA_URL, pathway)

    def format_value(self, value):
        print(value, type(value))
        if type(value) == str:
            value = json.loads(value)
            value['url'] = self.url(value['pathway'])
            return value

        return value.to_value()

    def get_context(self, name, value, attrs):
        context = super().get_context(name, value, attrs)
        return context

    class Media:
        css = {
            'all': ('pymedia/widget.css',)
        }
        js = ('pymedia/widget.js',)
