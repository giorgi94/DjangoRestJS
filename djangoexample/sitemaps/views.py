import datetime as dt
from django.contrib.sitemaps import Sitemap
from apps.blog.models import Blog


class BlogSitemap(Sitemap):
    changefreq = "weekly"
    priority = 1.0

    limit = 5  # per page limit items, ?p=1

    def items(self):
        objects = Blog.filter_blogs()
        return objects

    def lastmod(self, obj):
        return obj.updated


'''
class TagSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.9

    limit = 30000

    def items(self):
        return Tag.objects.all()


class CategorySitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8

    limit = 30000

    def items(self):
        return Category.objects.filter(published=True)


class AuthorSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8

    limit = 30000

    def items(self):
        return Author.objects.all()


class AuthorSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8

    limit = 30000

    def items(self):
        return Author.objects.all()
'''
