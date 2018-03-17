import os
import re
from django.shortcuts import (
    render, redirect, reverse,
    get_object_or_404
)
from django.http import (
    Http404, HttpResponse, JsonResponse
)
from django.utils.translation import ugettext_lazy as _

from django.apps import apps
from django.views import generic
from django.conf import settings
from django.contrib import messages


def page_not_found(request, *args, **kwargs):
    print(args, kwargs)
    return HttpResponse('<h1>Page not found</h1>')
