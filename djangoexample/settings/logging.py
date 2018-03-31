import os
import re
import sys
import json
import logging
import requests

from copy import copy
from django.core.mail import EmailMessage
from django.views.debug import ExceptionReporter

from django.conf import settings


class ServerErrorHandler(logging.Handler):

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

        message = extract_tags(message)

        # send_message_to_slack(message)
        # self.send_mail(subject, message, html_message)

    def send_mail(self, subject, message, html_message):
        try:
            msg = EmailMessage(
                subject,
                html_message,
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


MESSAGE_TAGS = [
    'Internal Server Error',
    'Request Method',
    'Request URL',
    # 'Django Version',
    # 'Python Executable',
    # 'Python Version',
    # 'Python Path',
    'Server time',
    # 'Installed Applications',
    # 'Installed Middleware',
    'Traceback',
    'Exception Type',
    'Exception Value',
    # 'Request information',
    'USER',
    # 'GET',
    # 'POST',
    # 'FILES',
    # 'COOKIES',
    # 'META',
    # 'Settings'
]


def extract_tags(message_lines_str):
    message = ""
    append = False

    for line in message_lines_str.split('\n'):
        tag = re.match(r'^[a-zA-Z\s]+(?=\:)', line)

        if tag:
            if tag.group() in MESSAGE_TAGS:
                append = True
                message += line.strip() + '\n'
            else:
                append = False
        elif append and line.strip():
            message += '\t' + line.strip() + '\n'
    return message


SLACK_WEBHOOK_URL = "https://hooks.slack.com/services/T00000000/B00000000/XXXXXXXXXXXXXXXXXXXXXXXX"


def send_message_to_slack(message):
    headers = {
        'content-type': 'application/json'
    }
    data = {
        'text': message,
    }
    r = requests.post(SLACK_WEBHOOK_URL, headers=headers, data=json.dumps(data), timeout=5)
    return r.status_code
