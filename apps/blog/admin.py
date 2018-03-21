from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from django.contrib import admin
from .models import Blog, Comment, Category
from .forms import BlogForm


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    exclude = ['alias']


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    form = BlogForm
    exclude = ['alias', ]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass
