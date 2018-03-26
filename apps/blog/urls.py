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

    path('search', views.BlogSearchView(), name="search"),
]
