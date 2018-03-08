from django.contrib import admin
from .models import User
# from django.db.models import Q

from django.contrib.auth.models import Permission
from django.contrib.sites.models import Site


class UserAdmin(admin.ModelAdmin):
    list_display = ['email', 'first_name', 'last_name']
    search_fields = ['email', 'first_name', 'last_name']

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        post_password = request.POST.get('password', '')

        if request.user.is_superuser and post_password.startswith('set:'):
            obj.set_password(post_password[4:])
            obj.save()

    def get_form(self, request, obj=None, **kwargs):
        if not request.user.is_superuser:
            self.exclude = ['password']

        return super().get_form(request, obj, **kwargs)

    class Meta:
        model = User


class PermissionAdmin(admin.ModelAdmin):
    search_fields = ['name', 'codename']


admin.site.register(User, UserAdmin)
admin.site.register(Permission, PermissionAdmin)
