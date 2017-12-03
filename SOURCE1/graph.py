# written by Vaishali

from abc import abstractmethod, ABCMeta

from six import add_metaclass

@add_metaclass(ABCMeta)
class Graph:
    _labels = []
    _sizes = []

    def __init__(self, data):
        self._data = data

    def get_Gender(self):
        self._labels = 'Male', 'Females'
        males = 0
        females = 0
        for row in self._data:
            if row[1] == 'M':
                males += 1
            else:
                females += 1
        self._sizes = [males, females]

    @abstractmethod
    def show_gender(self):
        pass

    @abstractmethod
    def show_BMI(self):
        pass
