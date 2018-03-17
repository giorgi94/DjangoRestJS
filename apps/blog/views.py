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

# LOG_FILENAME = settings.BASE_DIR + '/log/logging_example.log'
# logging.basicConfig(filename=LOG_FILENAME, level=logging.DEBUG)

# logging.debug('This message should go to the log file')


def print_exception(etype, value, tb, limit=None, file=None, chain=True):
    if file is None:
        file = sys.stderr
    for line in traceback.TracebackException(
            type(value), value, tb, limit=limit).format(chain=chain):
        print(line, file=file, end="")


def try_view_404(original_function):
    def wrapper_function(*args, **kwargs):
        try:
            return original_function(*args, **kwargs)
        except Exception as ex:
            # logging.exception('Got exception on main handler')
            exc_type, exc_value, exc_traceback = sys.exc_info()
            print_exception(exc_type, exc_value, exc_traceback,
                            limit=2, file=sys.stdout)

            raise Http404
    return wrapper_function


class IndexView(generic.TemplateView):
    template_name = 'home.html'

    @try_view_404
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # sdg
        return context


class BlogView(generic.TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context
