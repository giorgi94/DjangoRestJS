import os
import sys
import traceback
import logging
import re
import json
import pytz
import requests

from django.shortcuts import (
    render, redirect, reverse, get_object_or_404)
from django.http import (
    Http404, HttpResponse, JsonResponse)
from django.utils.translation import ugettext_lazy as _

from django.views import generic
from django.conf import settings
from .models import Blog

from haystack.query import SearchQuerySet
from haystack.views import SearchView


class IndexView(generic.TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['blog'] = Blog.objects.get(pk=20)
        context['blog2'] = Blog.objects.get(pk=21)
        return context


class BlogView(generic.TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context


class BlogSearchView(SearchView):
    template = 'search/search.html'
