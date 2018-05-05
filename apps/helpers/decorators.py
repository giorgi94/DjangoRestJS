import os
import json
from django.conf import settings
from django.core.cache import cache


def assure_path_exists(path):
    dir_path = os.path.dirname(path)
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)


def make_cache(key, timeout=None, overwrite=False):
    def decorator_function(original_function):
        def wrapper_function():
            CACHE_STATE = settings.CONFIG.get('cache', False)

            data = cache.get(key)

            if data and not overwrite:
                return data

            data = original_function()

            if CACHE_STATE and data:
                if timeout:
                    cache.set(key, data, timeout=timeout)
                else:
                    cache.set(key, data)

            return data
        return wrapper_function
    return decorator_function
