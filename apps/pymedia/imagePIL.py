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


def normilize_size(size):
    if type(size) == str:
        if re.fullmatch('\d+x\d+', size) is None:
            return None
        return eval('(' + size.replace('x', ',') + ')')
    else:
        return size


def placeholder(size):
    return 'http://via.placeholder.com/%s' % size


class ImagePIL:

    def __init__(self, path, point=(50, 50), quality=90):
        self.path = os.path.abspath(path)
        self.point = point
        self.quality = quality

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
            os.path.basename(self.path))
        dirname = os.path.dirname(self.path)

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

    def cover(self, size, point=None, safepath=None, overwrite=True):
        try:
            with Image.open(self.path) as img:
                if point is None:
                    point = self.point

                size = normilize_size(size)

                if point is None:
                    point = self.point

                if safepath is None:
                    safepath = self.safepath_isnull(size=size, method='cover', point=point)

                if not overwrite:
                    if os.path.isfile(safepath):
                        return (True, safepath)

                cover_size = self.get_cover_size(img.size, size)

                coords = self.get_coords_from_center(cover_size, size)
                coords = self.adjust_coords(coords, cover_size, point)

                img = img.resize(cover_size, Image.ANTIALIAS)
                img = img.crop(coords)

                assure_path_exists(safepath)

                img.save(safepath, subsampling=0, quality=self.quality, optimize=True)
                return (True, safepath)
            return (False,)
        except Exception as ex:
            print(ex)
            return (False,)

    def fit(self, size, safepath=None, overwrite=True):
        try:
            with Image.open(self.path) as img:
                size = normilize_size(size)

                if safepath is None:
                    safepath = self.safepath_isnull(size=size, method='fit')

                if not overwrite:
                    if os.path.isfile(safepath):
                        return (True, safepath)

                fit_size = self.get_fit_size(img.size, size)
                img = img.resize(fit_size, Image.ANTIALIAS)

                assure_path_exists(safepath)

                img.save(safepath, subsampling=0, quality=self.quality, optimize=True)

                return (True, safepath)
            return (False,)
        except Exception as ex:
            print(ex)
            return (False,)


if __name__ == '__main__':

    img = ImagePIL(os.path.abspath('img.jpg'))
    img.fit((300, 230))
    img.cover((300, 230), point=(50, 10))
    img.cover('300x230', point=(50, 10))
