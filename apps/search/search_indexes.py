from haystack import indexes
from apps.blog.models import Blog


class BlogIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(
        document=True, use_template=True,
        template_name='search/indexes/blog/blog_text.txt')
    title = indexes.CharField(model_attr='title')
    content = indexes.CharField(model_attr='content')

    def get_model(self):
        return Blog

    def index_queryset(self, using=None):
        return self.get_model().objects.all()
