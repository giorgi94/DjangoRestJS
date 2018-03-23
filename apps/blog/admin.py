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

    def save_model(self, request, obj, form, change):
        print(form.is_valid())
        print(request.POST)

        # super().save_model(request, obj, form, change)
        # if obj.image:
        #     if obj.image.startswith('http://cdn.ambebi.ge/media/'):
        #         obj.image = obj.image.replace('http://cdn.ambebi.ge/media/', '')
        #         obj.save()
        # if settings.CACHE_STATE and settings.CACHE_IP_HOST:
        #     client.clear_cache_jsons(request, obj.pk, settings.CACHE_IP_HOST)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass
