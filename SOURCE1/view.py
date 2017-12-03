# written by Vaishali

from abc import abstractmethod, ABCMeta

from six import add_metaclass

@add_metaclass(ABCMeta)
class View:
    @staticmethod
    def output(data):
        """
        Outputs the data to the console or terminal
        """
        for row in data:
            print(', '.join(row))

    @abstractmethod
    def get_input(self, message):
        pass

    @abstractmethod
    def save_data_to_new(self, file_name, data_list):
        pass
