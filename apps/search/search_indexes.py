import os
from haystack import indexes
from apps.blog.models import Blog


class BlogSearchIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)

    title = indexes.CharField(model_attr='title')
    content = indexes.EdgeNgramField(model_attr='content')
    image = indexes.CharField(model_attr='img_dump')
    published = indexes.DateTimeField(model_attr='published')

    def get_model(self):
        return Blog

    def index_queryset(self, using=None):
        model = self.get_model()
        return model.objects.filter(model.default_Q())
