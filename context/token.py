import jwt
import base64
import datetime as dt
from django.shortcuts import Http404
from django.conf import settings


def generate(data=None):
    key = settings.TOKEN_SECRET_KEY
    data = {
        'exp': dt.datetime.utcnow() + dt.timedelta(seconds=60)
    }
    tk = jwt.encode(data, key, algorithm='HS256').decode()
    return tk


def validate(tk=None):
    try:
        key = settings.TOKEN_SECRET_KEY
        data = jwt.decode(tk, key, algorithms='HS256')
        return True
    except jwt.ExpiredSignatureError:
        return False
    except Exception as ex:
        return False


def validate_view(request):
    if settings.ON_LOCALHOST:
        return True

    tk = request.GET.get('token')
    if not validate(tk=tk):
        raise Http404
