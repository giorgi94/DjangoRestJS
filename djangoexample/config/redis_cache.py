USE_REDIS = False


REDIS_CHACHE_CONFIG = {
    "BACKEND": "django_redis.cache.RedisCache",
    "LOCATION": "redis://127.0.0.1:6379/0",
    "OPTIONS": {
        "CLIENT_CLASS": "django_redis.client.DefaultClient",
        "COMPRESSOR": "django_redis.compressors.zlib.ZlibCompressor",
        "SOCKET_CONNECT_TIMEOUT": 5,  # in seconds
        "SOCKET_TIMEOUT": 5,  # in seconds
        "IGNORE_EXCEPTIONS": True,
    }
}
