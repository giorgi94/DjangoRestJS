import re
import json
import pytz
import requests
from django.utils.dateparse import parse_datetime
from django.utils.html import strip_tags
from aide.clean_up_html import sanitize_html
from django.shortcuts import (
    render, redirect, reverse,
    get_object_or_404
)
from django.http import (
    Http404, HttpResponse, JsonResponse
)
from django.utils.translation import ugettext_lazy as _

from django.views import generic
from django.conf import settings
from django.contrib import messages
from django.db.models import Q
from django.utils import timezone as tz
from django.contrib.sites.shortcuts import get_current_site


class BlogView(generic.TemplateView):
    template_name = 'pages/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context
