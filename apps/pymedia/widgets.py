from django.utils.safestring import mark_safe
from django.forms import widgets


class ImagePILWidget(widgets.TextInput):
    template_name = 'pymedia/image_widget.html'

    def format_value(self, value):
        return value.to_value()

    def get_context(self, name, value, attrs):
        context = super().get_context(name, value, attrs)
        return context

    class Media:
        css = {
            'all': ('pymedia/widget.css',)
        }
        js = ('pymedia/widget.js',)
