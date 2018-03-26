from haystack import indexes
from .models import Blog


class NoteIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)

    title = indexes.CharField(model_attr='title')
    content = indexes.CharField(model_attr='content')

    def get_model(self):
        return Blog

    def index_queryset(self, using=None):
        model = self.get_model()
        return model.objects.filter(model.default_Q())
