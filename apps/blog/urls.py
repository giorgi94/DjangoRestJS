from django.urls import path, re_path
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from . import views

app_name = "blog"

urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),

    re_path(r'^blog/(?P<pk>[\d]+)$',
            views.BlogView.as_view(), name="blog-pk"),
    re_path(r'^blog/(?P<pk>[\d]+)-(?P<alias>[\w\-]+)$',
            views.BlogView.as_view(), name="blog"),

    re_path(r'^category/(?P<alias>[\w\-]+)$',
            views.BlogView.as_view(), name="category"),

    re_path(r'^tag/(?P<name>[\w\s]+)$',
            views.BlogView.as_view(), name="tag"),

    path('search', views.BlogSearchView.as_view(), name="search"),
]
