from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from django.contrib import admin
from .models import Blog
from .forms import BlogForm


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    form = BlogForm
    exclude = ['alias']

    # admin.site.register(BLog)
