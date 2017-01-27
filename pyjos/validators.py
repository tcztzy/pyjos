from numbers import Number
from enum import IntEnum

from .exceptions import ValidationError


class BaseValidator(object):
    def __call__(self, value):
        raise NotImplementedError


class NumberValidator(BaseValidator):
    def __call__(self, value):
        if isinstance(value, Number):
            return True
        raise ValidationError


class IntegerValidator(NumberValidator):
    def __call__(self, value):
        if super(IntegerValidator, self).__call__(value) and isinstance(value, int):
            return True
        raise ValidationError
