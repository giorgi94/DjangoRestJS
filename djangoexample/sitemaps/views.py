import datetime as dt
from django.contrib.sitemaps import Sitemap
from apps.blog.models import Blog, Category, Tag


class BlogSitemap(Sitemap):
    changefreq = "weekly"
    priority = 1.0

    limit = 5  # per page limit items, ?p=1

    def items(self):
        objects = Blog.objects.filter(Blog.default_Q())
        return objects

    def lastmod(self, obj):
        return obj.published


class TagSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.9

    limit = 5

    def items(self):
        return Tag.objects.all()


class CategorySitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8

    limit = 5

    def items(self):
        return Category.objects.filter(Category.default_Q())
