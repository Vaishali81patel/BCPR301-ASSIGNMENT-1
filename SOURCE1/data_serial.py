# created by Vaishali

from abc import abstractmethod, ABCMeta

from six import add_metaclass

@add_metaclass(ABCMeta)
class DataSerial:
    """
    Base class for DataCSV
    """
    def __init__(self, data_in):
        self._data = data_in

    @abstractmethod
    def unpack_data(self):
        pass;

    @abstractmethod
    def pack_data(self):
        pass

    def get_data(self):
        return self._data