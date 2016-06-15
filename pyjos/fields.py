import six


class Field(object):
    def __init__(self, *args, **kwargs):
        super(Field, self).__init__()


class StringField(Field):
    def __init__(self, max_length, default='', *args, **kwargs):
        if isinstance(max_length, six.integer_types):
            self.max_length = max_length
        else:
            raise ValueError('max_length should be integer types')
        if isinstance(default, six.string_types):
            self.value = default
        else:
            raise ValueError('default should be string types')
        super(StringField, self).__init__(*args, **kwargs)

    def __get__(self, instance, owner):
        print('get')
        return self.value

    def __set__(self, instance, value):
        print('set')
        if not isinstance(value, six.string_types):
            raise ValueError('Require string type objects')
        if len(value) > self.max_length:
            raise ValueError('String length is out of range')
        self.value = value


class TimeStampField(StringField):
    pass
