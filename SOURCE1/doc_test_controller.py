# created by Vaishali
"""
Doc test for the command_view class

Tests are run for function return values in controller.py

>>> ctrl = Controller(view_list, cmd_view, Employee())
>>> ctrl.check_valid_file_name('data/data_employee.db', 'input')
True

>>> ctrl.check_valid_file_name('employee.xx', 'input')
File does not exist
False

>>> ctrl.check_file_exists('ddata_employee.dbe.db')
False

>>> ctrl.check_file_exists("xxx.csv")
False

>>> ctrl.check_file_name_extensions("xxx.db", 'input')
True

>>> ctrl.check_file_name_extensions("xxx.csv", 'input')
True

>>> ctrl.check_file_name_extensions("xxx.pickle", 'input')
True

>>> ctrl.check_file_name_extensions("xxx.xx", 'input')
File name must end with:
csv
db
pickle
False
"""

from controller import Controller
from employee import Employee
from command_view import CommandView
from view_csv_file import CsvFileView
from view_database import DatabaseView
from view_pickle import PickleView

cmd_view = CommandView()
csv_view = CsvFileView()
pickle_view = PickleView()
database_view = DatabaseView()
view_list = [csv_view, database_view, pickle_view]


if __name__ == "__main__":
    import doctest
    doctest.testmod()
