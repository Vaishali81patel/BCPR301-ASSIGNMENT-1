# Created by Vaishali

from abc import abstractmethod, ABCMeta

from six import add_metaclass

@add_metaclass(ABCMeta)
class ValidateField():
    _valid = "Valid"

    def __init__(self, field):
        self._field = field

    @abstractmethod
    def validate(self):
        pass

    def get_field(self):
        return self._field
