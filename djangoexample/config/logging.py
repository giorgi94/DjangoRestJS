import os
import sys
import logging
import traceback
from copy import copy
from django.views.debug import ExceptionReporter
from django.core.mail import EmailMessage
from django.template.loader import render_to_string

from django.conf import settings


class ServerErrorEmailHandler(logging.Handler):

    def __init__(self, include_html=False, email_backend=None):
        logging.Handler.__init__(self)

    def emit(self, record):
        try:
            request = record.request
            subject = '%s: %s' % (
                record.levelname,
                record.getMessage()
            )
        except Exception:
            subject = '%s: %s' % (
                record.levelname,
                record.getMessage()
            )
            request = None
        subject = self.format_subject(subject)

        # Since we add a nicely formatted traceback on our own, create a copy
        # of the log record without the exception data.
        no_exc_record = copy(record)
        no_exc_record.exc_info = None
        no_exc_record.exc_text = None

        if record.exc_info:
            exc_info = record.exc_info
        else:
            exc_info = (None, record.getMessage(), None)

        reporter = ExceptionReporter(request, is_email=True, *exc_info)
        message = "%s\n\n%s" % (self.format(no_exc_record), reporter.get_traceback_text())
        html_message = reporter.get_traceback_html()

        # with open('error.html', 'w') as f:
        #     f.write(html_message)

        self.send_mail(subject, html_message, fail_silently=True, html_message=html_message)

    def send_mail(self, subject, message, *args, **kwargs):
        try:
            msg = EmailMessage(
                subject,
                message,
                settings.EMAIL_HOST_USER,
                settings.EMAIL_SERVER_ERROR
            )
            msg.content_subtype = "html"
            msg.send()
        except Exception as ex:
            print('Email was not sent')
            print(ex)

    def format_subject(self, subject):
        """
        Escape CR and LF characters.
        """
        return subject.replace('\n', '\\n').replace('\r', '\\r')
