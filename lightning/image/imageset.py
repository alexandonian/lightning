import logging
from numpy import ndarray, arange, amax, amin, size, asarray, random, prod, \
    apply_along_axis
from itertools import product

from ..base import Data


class ImageSet(Data):
    """
    A set of images or volumes

    Backed by an array-like object, including a numpy array
    (for local computation) or a bolt array (for spark computation).

    Attributes
    ----------
    values : array -like
        numpy array of bolt array.

    labels : array-like or list
        A set of labels, one per channel.
    """
    _metadata = Data._metadata

    def __init__(self, values, label=None, mode='local'):
        super(ImageSet, self).__init__(values, labels=None, mode='local')
        self.labels = labels
        if values is not None:
            self.images = values

    def max(self):
        pass

    def tospark(self):
        pass

    def mean(self):
        pass

    def baseaxes(self):
        pass

    def min(self):
        pass

    def count(self):
        pass

    def sum(self):
        pass

    def tolocal(self):
        pass

    def map(self, func, **kwargs):
        pass

    def std(self):
        pass

    def first(self):
        pass

    def var(self):
        pass
