import collections.abc as abc


class MapBase(abc.MutableMapping):
    class _Item:
        __slots__ = "key", "value"

        def __init__(self, key, value):
            self._key = key
            self._value = value

        def __eq__(self, other):
            return self._key == other

        def __ne__(self, other):
            return not (self == other)

        def __lt__(self, other):
            return self._key < other._key

    def __getitem__(self, item):
        pass

    def __setitem__(self, key, value):
        pass

    def __delitem__(self, key):
        pass

    def __iter__(self):
        pass

    def __len__(self):
        pass
