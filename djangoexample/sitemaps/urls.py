from django.urls import path
from django.contrib.sitemaps.views import sitemap


from .feed import *
from .views import *


app_sitemaps = "sitemaps"

urlpatterns = [
    path('feed.xml', BlogFeed(), name="feed"),
    path('<str:section>.xml', sitemap,
         {
             'sitemaps': {
                 'blogs': BlogSitemap,
                 # 'tags': TagSitemap,
                 # 'authors': AuthorSitemap,
             }
         },
         name='django.contrib.sitemaps.views.sitemap'),

]
