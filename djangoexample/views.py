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

from datetime import datetime
from django.utils import timezone as tz

from apps.serializer import getArticleDetailSerializer

Article = apps.get_model('articles', 'Article')



