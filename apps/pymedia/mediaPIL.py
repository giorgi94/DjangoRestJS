import os
from .imagePIL import (
    ImagePIL, download,
    normilize_point, normilize_size)
from django.conf import settings

BASE_DIR = settings.BASE_DIR
MEDIA_DIR = settings.MEDIA_ROOT
MEDIA_URL = settings.MEDIA_URL


def reverse(path, method, size, point=None):
    basename = os.path.basename(path)
    filename, ext = os.path.splitext(basename)
    size = normilize_size(size)

    if not point is None:
        point = normilize_point(point)

        return '__thumbs__/{method}/{size}/{filename}__{point}{ext}'.format(
            method=method, filename=filename, ext=ext,
            point="%dx%d" % point, size="%dx%d" % size)

    return '__thumbs__/{method}/{size}/{filename}{ext}'.format(
        method=method, filename=filename, ext=ext,
        size="%dx%d" % size)


class MediaPIL(ImagePIL):

    BASE_DIR = BASE_DIR
    MEDIA_DIR = MEDIA_DIR
    MEDIA_URL = MEDIA_URL

    def __init__(self, path):
        self._path = os.path.join(MEDIA_DIR, path)

    @staticmethod
    def placeholder(size):
        return 'http://via.placeholder.com/%s' % size

    @staticmethod
    def download(url, to='downloads', timeout=5):
        to = os.path.join(MEDIA_DIR, to)
        return download(url, to, timeout)

    @staticmethod
    def reverse(path, method="cover", size="10x10", point=None):
        return reverse(path, method, size, point)

    def safepath_isnull(self, size, method, point=None):
        path = reverse(self._path, method, size, point)
        return os.path.join(MEDIA_DIR, path)


if __name__ == '__main__':
    pass
    # MediaPIL.download(url, to=".")
