from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import (
    render, redirect, reverse, get_object_or_404)
from django.http import Http404, JsonResponse
from django.utils.translation import ugettext_lazy as _

from django.views import generic
from django.conf import settings
from .models import Blog

from apps.search.query import SearchMixin
from apps.graphQL.schema import schema
from apps.graphQL.base64enc import encode, decode
from django.core.cache import cache


class IndexView(generic.TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['blog'] = Blog.objects.get(pk=20)
        context['blog2'] = Blog.objects.get(pk=21)
        return context


class BlogView(generic.TemplateView):
    template_name = 'blog.html'

    def get_object(self):
        blog = cache.get('BlogNode:23')

        if blog:
            return blog

        query = '''{{
                blog(id:"{id}") {{
                    pk,
                    title,
                    content,
                    commentSet {{
                        edges {{
                            node {{
                                content
                            }}
                        }}
                    }}
                }}
            }}'''.format(id=encode('BlogNode:23'))

        blog = schema.execute(query).data

        if blog:
            blog = blog.get('blog')
            cache.set('BlogNode:23', blog, timeout=5)
            return blog
        return None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['blog'] = self.get_object()
        return context


class BlogSearchView(SearchMixin, generic.TemplateView):
    template_name = 'search.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['searched_data'] = self.get_searched_data()
        return context


@staff_member_required
def queryCategory(request, **kwargs):

    return JsonResponse({'hello': 'It works'})
