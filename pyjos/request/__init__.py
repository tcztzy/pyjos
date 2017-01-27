import json

from . import service

__all__ = ['BaseRequest', 'parameter']


class BaseRequest(object):
    _api_params = {}

    def __init__(self, **kwargs):
        for k, v in kwargs:
            setattr(self, '_'+k, v)

    @property
    def api_params(self):
        return json.dumps(self._api_params)


def getter(attr, default=None):
    def _getter(self):
        return getattr(self, attr, default)
    return _getter


def setter(attr, validators=None):
    def _setter(self, value):
        if all(map(lambda validator: validator(value), validators)):
            setattr(self, attr, value)
            self._api_params[attr] = value
    return _setter


def deleter(attr):
    def _deleter(self):
        delattr(self, attr)
        del self._api_params[attr]
    return _deleter


def parameter(attr, default=None, validators=None, doc=""):
    return property(getter(attr, default),
                    setter(attr, validators),
                    deleter(attr), doc)
