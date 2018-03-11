from django import forms
from .models import Blog


class BlogForm(forms.ModelForm):

    class Meta:
        model = Blog
        fields = '__all__'
        widgets = {
            'content': forms.Textarea(attrs={'rich-editor': 'true'}),
        }
