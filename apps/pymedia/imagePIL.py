import os
import re
import requests

from PIL import Image


def assure_path_exists(path):
    dir_path = os.path.dirname(path)
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)


def download(url, to='downloads', timeout=5):
    try:
        r = requests.get(url, timeout=timeout)

        filename = os.path.basename(url)
        to = os.path.abspath(to)
        path = os.path.join(to, filename)
        assure_path_exists(path)

        f = open(path, 'bw')
        f.write(r.content)
        f.close()
        return path
    except Exception as ex:
        print(ex)
        return None


def normilize_point(point):
    try:
        if re.fullmatch('(\(\d{1,2},\d{1,2}\))|(\d{1,2}x\d{1,2})', str(point).replace(' ', '')) is None:
            return self._default_point
        else:
            if type(point) == str:
                if 'x' in point:
                    return eval('(' + point.replace('x', ',') + ')')
                return eval(point)
            return point
    except:
        return self._default_point


def normilize_size(size):
    try:
        if re.fullmatch('(\(\d+,\d+\))|(\d+x\d+)', str(size).replace(' ', '')) is None:
            return (10, 10)
        else:
            if type(size) == str:
                if 'x' in size:
                    return eval('(' + size.replace('x', ',') + ')')
                return eval(size)
            return size
    except:
        return (10, 10)


def placeholder(size):
    return 'http://via.placeholder.com/%s' % size


def reverse(path, method, size, point):
    size = imagePIL.normilize_size(size)
    point = imagePIL.normilize_size(point)

    if size is None or point is None:
        return None

    filepath, ext = os.path.splitext(path)

    return '__thumbs__/{method}/{size}/{filepath}__{point}.{ext}'.format(
        method=method, filepath=filepath, ext=ext,
        point="%dx%d" % point, size="%dx%d" % size)


class ImagePIL:

    _default_point = (50, 50)
    _quality = 90

    def __init__(self, path=None):
        self._path = os.path.abspath(path)

    def set_path(self, path):
        self._path = os.path.abspath(path)

    def set_default_point(self, point):
        self._default_point = normilize_point(point)

    def get_cover_size(self, from_size, to_size):
        p = max(
            to_size[0] / from_size[0],
            to_size[1] / from_size[1]
        )
        return (int(p * from_size[0]), int(p * from_size[1]))

    def get_fit_size(self, from_size, to_size):
        p = min(
            to_size[0] / from_size[0],
            to_size[1] / from_size[1]
        )
        return (int(p * from_size[0]), int(p * from_size[1]))

    def get_coords_from_center(self, from_size, to_size):
        coords = (
            int((from_size[0] - to_size[0]) / 2),
            int((from_size[1] - to_size[1]) / 2),
            int((from_size[0] + to_size[0]) / 2),
            int((from_size[1] + to_size[1]) / 2)
        )
        return coords

    def adjust_coords(self, coords, size, point):
        vec = [
            size[0] * (point[0] - 50) / 100,
            size[1] * (point[1] - 50) / 100
        ]
        if coords[0] + vec[0] < 0:
            vec[0] = - coords[0]
        if coords[1] + vec[1] < 0:
            vec[1] = - coords[1]
        if coords[3] + vec[1] > size[1]:
            vec[1] = size[1] - coords[3]
        if coords[2] + vec[0] > size[0]:
            vec[0] = size[0] - coords[2]
        return tuple([int(sum(coord)) for coord in zip(coords, 2 * vec)])

    def safepath_isnull(self, size, method, point=None):
        basename, extension = os.path.splitext(
            os.path.basename(self._path))
        dirname = os.path.dirname(self._path)

        if point is None:
            filename = (basename + '__{0}'.format(method) +
                        '__{0}x{1}'.format(*size) +
                        extension)
        else:
            filename = (basename + '__{0}'.format(method) +
                        '__{0}x{1}'.format(*size) +
                        '__{0}x{1}'.format(*point) +
                        extension)

        return os.path.join(dirname, '__thumb__', filename)

    def cover(self, size, point, safepath=None):
        try:
            with Image.open(self._path) as img:
                size = normilize_size(size)
                point = normilize_point(point)

                cover_size = self.get_cover_size(img.size, size)

                coords = self.get_coords_from_center(cover_size, size)
                coords = self.adjust_coords(coords, cover_size, point)

                img = img.resize(cover_size, Image.ANTIALIAS)
                img = img.crop(coords)

                if safepath is None:
                    safepath = self.safepath_isnull(size=size, method='cover', point=point)
                assure_path_exists(safepath)

                img.save(safepath, subsampling=0, quality=self._quality, optimize=True)
                return True
            return False
        except Exception as ex:
            print(ex)
            return False

    def fit(self, size, safepath=None):
        try:
            with Image.open(self._path) as img:
                size = normilize_size(size)

                fit_size = self.get_fit_size(img.size, size)
                img = img.resize(fit_size, Image.ANTIALIAS)

                if safepath is None:
                    safepath = self.safepath_isnull(size=size, method='fit')
                assure_path_exists(safepath)

                img.save(safepath, subsampling=0, quality=self._quality, optimize=True)

                return True
            return False
        except Exception as ex:
            print(ex)
            return False


if __name__ == '__main__':

    img = ImagePIL(os.path.abspath('img.jpg'))
    img.fit((300, 230))
    img.cover((300, 230), point=(50, 70))
