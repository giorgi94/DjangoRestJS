from django import forms
from .models import Blog


class BlogAdminForm(forms.ModelForm):

    class Meta:
        model = Blog
        fields = '__all__'
        widgets = {
            'content': forms.Textarea(attrs={'rich-editor': 'true'}),
            'tags': forms.SelectMultiple(attrs={'class': 'ui dropdown search'})
        }

    class Media:
        js = ('tinymce/tinymce.config.js',)
