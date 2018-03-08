from django.urls import include, path
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

from django.contrib.auth.decorators import login_required
from graphene_django.views import GraphQLView

# from . import views

admin.site.site_header = settings.SITE_NAME

urlpatterns = [
    path('sitemaps/', include('djangoexample.sitemaps.urls')),

    path('graphql', GraphQLView.as_view(graphiql=True)),

    path('', include('apps.blog.urls')),

    path('admin/', admin.site.urls),
    path('i18n/', include('django.conf.urls.i18n')),


]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG and settings.DEBUG_TOOLS:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
