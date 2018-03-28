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
    published = indexes.DateTimeField(model_attr='published')

    def get_model(self):
        return Blog

    def index_queryset(self, using=None):
        model = self.get_model()
        return model.objects.filter(model.default_Q())


def searchQuery(qstring, page=1, pagelen=5,
                sortedby="published", reverse=True):
    ix = index.open_dir(whoosh_dir)

    qp = qparser.QueryParser("text", schema=ix.schema)
    q = qp.parse(qstring)

    with ix.searcher() as s:
        results = s.search_page(q, page, pagelen=pagelen,
                                sortedby=sortedby, reverse=reverse)
        if not results:
            corrected = s.correct_query(q, qstring)
            results = s.search_page(corrected.query, page, pagelen=pagelen,
                                    sortedby=sortedby, reverse=reverse)
        return {
            'pagination': {
                'total': results.total,
                'pagenum': results.pagenum,
                'pagelen': results.pagelen,
                'offset': results.offset
            },
            'query': [dict(result) for result in results]
        }


class SearchMixin:
    pagelen = 5
    reverse = True
    sortedby = "published"
    q_min_length = 3
    query_kwarg = 'q'
    page_kwarg = 'page'

    def get_search_results(self, q, page=1):
        if len(q) < self.q_min_length:
            return None
        return searchQuery(q, page,
                           pagelen=self.pagelen,
                           sortedby=self.sortedby,
                           reverse=self.reverse)

    def get_searched_data(self):
        q = self.request.GET.get(self.query_kwarg, '')
        page = self.request.GET.get(self.page_kwarg, 1)
        if type(page) == str:
            page = int(page)
        return self.get_search_results(q, page)
