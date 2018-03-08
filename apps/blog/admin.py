from django.utils.translation import ugettext_lazy as _
from django.contrib import admin
from django import forms
from .models import *
from django.conf import settings


class BlogForm(forms.ModelForm):

    class Meta:
        model = Blog
        fields = '__all__'
        widgets = {
            'content': forms.Textarea(attrs={'rich-editor': 'true'}),
        }


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    form = BlogForm
    exclude = ['alias']

    # admin.site.register(BLog)
