# written by Vaishali

from abc import abstractmethod, ABCMeta

from six import add_metaclass


@add_metaclass(ABCMeta)
class Model:
    def __init__(self):
        pass

    @abstractmethod
    def employee_info(self, data):
        pass
