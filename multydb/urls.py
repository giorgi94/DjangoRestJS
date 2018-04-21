from django.contrib import admin
from django.urls import include, path

from django.conf.urls.i18n import i18n_patterns
from app.views import *

urlpatterns = [
    
    path('admin/', admin.site.urls),
    path('i18n/', include('django.conf.urls.i18n')),
]


urlpatterns += i18n_patterns(
    path('', index, name="index"),
    path('register', register, name="register")
)