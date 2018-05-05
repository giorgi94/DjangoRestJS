import os
import json
from django.conf import settings
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer


CACHE_DIR = settings.CACHE_DIR
CACHE_STATE = settings.CACHE_STATE


def assure_path_exists(path):
    dir_path = os.path.dirname(path)
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)


def CacheRead(dirname, filename):
    try:
        path = "{0}/{1}/{2}.json".format(CACHE_DIR, dirname, filename)

        if os.path.isfile(path):
            with open(path, 'rb') as cache_reader:
                data = cache_reader.read()
            return json.loads(data)
        return None
    except:
        return None


def CacheCreate(dirname, filename, data):
    try:
        path = "{0}/{1}/{2}.json".format(CACHE_DIR, dirname, filename)

        assure_path_exists(path)

        with open(path, 'wb') as cache_writer:
            cache_writer.write(JSONRenderer().render(data))

        return True
    except:
        return False


def ClearCache(dirname, filename):
    try:
        path = "{0}/{1}/{2}.json".format(CACHE_DIR, dirname, filename)

        if os.path.isfile(path):
            os.remove(path)

        return True
    except:
        return False


# decorators
def cache_data_to_json(dirname, filename, overwrite=False):
    def decorator_function(original_function):
        def wrapper_function():
            if CACHE_STATE:
                cache = CacheRead(dirname, filename)
                if cache and not overwrite:
                    return cache

            data = original_function()

            if CACHE_STATE:
                CacheCreate(dirname, filename, data)

            return data
        return wrapper_function
    return decorator_function
