from django.urls import path
from django.contrib.sitemaps.views import sitemap


from .feed import *
from .views import *

urlpatterns = [
    path('feed', BlogFeed(), name="feed"),
    path('<str:section>.xml', sitemap,
         {
             'sitemaps': {
                 'articles': BlogSitemap,
                 # 'tags': TagSitemap,
                 # 'authors': AuthorSitemap,
             }
         },
         name='django.contrib.sitemaps.views.sitemap'),

]
