from abc import ABCMeta, abstractclassmethod


class Backend(object):
    __metaclass__ = ABCMeta

    @abstractclassmethod
    def set(self, key, value, **kwargs):
        pass

    @abstractclassmethod
    def get(self, key, default=None, **kwargs):
        pass

    @abstractclassmethod
    def remove(self, **kwargs):
        pass
