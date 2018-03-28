import os

from haystack import indexes
from whoosh import index, qparser

from django.conf import settings
from .models import Blog

whoosh_dir = settings.WHOOSH_INDEX


class BlogSearchIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)

    title = indexes.CharField(model_attr='title')
    content = indexes.EdgeNgramField(model_attr='content')

    published = indexes.DateTimeField(model_attr='published', faceted=True)

    suggestions = indexes.FacetCharField()

    def get_model(self):
        return Blog

    def index_queryset(self, using=None):
        model = self.get_model()
        return model.objects.filter(model.default_Q())

    def prepare(self, obj):
        prepared_data = super().prepare(obj)
        prepared_data['suggestions'] = prepared_data['text']
        return prepared_data


def blogSearchQuery(qstring, limit=20, sortedby="published", reverse=True):
    ix = index.open_dir(whoosh_dir)

    qp = qparser.QueryParser("text", schema=ix.schema)
    q = qp.parse(qstring)

    query = []

    with ix.searcher() as s:
        results = s.search(q, limit=limit, sortedby=sortedby, reverse=reverse)

        if not results:
            corrected = s.correct_query(q, qstring)
            results = s.search(corrected.query,
                               limit=limit, sortedby=sortedby, reverse=reverse)
        query = [dict(result) for result in results]
    return query
