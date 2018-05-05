from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from django.contrib import admin
from .models import Blog, Comment, Category, Tag
from .forms import BlogAdminForm


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    exclude = ('alias', )


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    form = BlogAdminForm
    exclude = ('alias', )

    # raw_id_fields = ('tags', )


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass


admin.site.register(Tag)
