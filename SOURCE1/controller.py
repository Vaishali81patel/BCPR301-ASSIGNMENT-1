# Written by Vaishali

from sys import argv
from graph_pie import PieChart
from graph_bar import BarChart
import os


class Controller(object):
    _input_view = ''
    _view_list = ''
    _output_view = ''
    _data_list = []
    _extension_types = ['csv', 'db', 'pickle']

    def __init__(self, view_list, command_view, model):
        """
        Initialises the views and model
        :view_list: a list of types of user choose views available
        :command_view: the cmd view
        :model: the employee model
        """
        self._view_list = view_list
        self.command_view = command_view
        self.model = model

    def start(self):  
        """
        Checks to see if line orientated or command line
        """
        if len(argv) > 1:
            self.command_view.onecmd(' '.join(argv[1:]))
        else:
            self.command_view.cmdloop()

    def open_file_and_validate(self, file_name):
        """
        Checks to make sure it is a valid file
        If it is a valid file it open the file and puts it into a list
        Validates the records and fields in the file
        Drops any invalid records and returns an error list if necessary
        :file_name:
        :return: error list
        """

        if self.get_list_of_data_objects(file_name):
            # send the input to be validated
            self._data_list, error_list = self.model.employee_info(self._data_list)
            if not error_list:
                print(file_name, "Inputted with no errors")
            else:
                print("Records with errors dropped:")

            # print out errors that caused the records to be dropped
            self._input_view.output(error_list)

    def show_graph(self, file_name, the_type):
        """
        Shows a graph of the gender types
        :file_name:
        :the_type:
            default value bar_chart
            possible values: pie, bar_chart
        :return:
        """
        if self.get_list_of_data_objects(file_name):
            # sends data off to a graph object
            if the_type == "pie":
                graph = PieChart(self._data_list)
                graph.get_Gender()
                graph.show_gender()  # pragma: no cover
            else:
                graph = BarChart(self._data_list)
                graph.get_Gender()
                graph.show_gender()  # pragma: no cover

    def save_data_to_new_file(self, file_name):
        """
        Checks that the filename is not already in use
        Validates the extension as a valid type
        Saves the data to the new file name
        :file_name: format - file_name.extension
            valid extensions - .csv, .db, .pickle
        :return:
        """
        succeed = False
        if self._data_list:
            succeed = self.save_data_if_valid_file(file_name)
        else:
            print("There is no data present. "
                  "Use 'file <filename>' to input data")
        return succeed

    def save_data_if_valid_file(self, file_name):
        succeed = False
        if self.check_file_exists(file_name):
            print("File already exists, choose a different file name.")
        else:
            if self.check_file_name_extensions(file_name, 'output'):
                # do the actual saving
                self._output_view.save_data_to_new(file_name, self._data_list)
                succeed = True
        return succeed

    def show_records(self):
        result = False
        for i in self._data_list:
            result = True
            print(i)
        return result

    def get_list_of_data_objects(self, file_name):
        if self.check_valid_file_name(file_name, 'input'):
            self._data_list = self._input_view.get_input(file_name)
            return True
        else:
            return False

    def check_valid_file_name(self, file_name, input_output):
        """
        Checks to make sure the file_name exists and if it
        has a valid file extension
        :file_name:
        :input_output:
        :return:
        """
        if self.check_file_exists(file_name):
            if self.check_file_name_extensions(file_name, input_output):
                return True
            else:
                return False
        else:
            print("File does not exist")
            return False

    def check_file_name_extensions(self, file_name, input_output):
        """
        Checks the file extension against the possible extensions set up
        in the class variable _extension_types
        :file_name:
        :input_output:
        :return:
        """
        for i in self._extension_types:
            if file_name.endswith(i):
                _index = self._extension_types.index(i)
                if input_output == 'input':
                    self._input_view = self._view_list[_index]
                else:
                    self._output_view = self._view_list[_index]
                return True
        print("File name must end with:")
        for i in self._extension_types:
            print(i)
        return False

    @staticmethod
    def check_file_exists(file_name):
        """
        Checks to make sure the file exists
        :file_name:
        :return:
        """
        if os.path.isfile(file_name):
            return True
        else:
            return False
