from django.contrib.syndication.views import Feed

from apps.blog.models import Blog


class BlogFeed(Feed):
    title = '...'
    description = '...'

    def items(self):
        return Blog.objects.all()[:20]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.abstract

    def item_pubdate(self, item):
        return item.created
