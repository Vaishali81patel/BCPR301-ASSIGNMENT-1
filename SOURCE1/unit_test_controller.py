# written by Vaishali
"""
Does unit tests for the command view
"""

import unittest
from controller import Controller
from employee import Employee
from command_view import CommandView
from view_csv_file import CsvFileView
from view_database import DatabaseView
from view_pickle import PickleView
import sys
from contextlib import contextmanager
from io import StringIO
import os


class ControllerUnitTests(unittest.TestCase):
    def setUp(self):
        cmd_view = CommandView()
        csv_view = CsvFileView()
        pickle_view = PickleView()
        database_view = DatabaseView()
        view_list = [csv_view, database_view, pickle_view]
        self.ctrl = Controller(view_list, cmd_view, Employee())

    def tearDown(self):
        print("This test case is done!")

    @contextmanager
    def captured_output(self):
        new_out, new_err = StringIO(), StringIO()
        old_out, old_err = sys.stdout, sys.stderr
        try:
            sys.stdout, sys.stderr = new_out, new_err
            yield sys.stdout, sys.stderr
        finally:
            sys.stdout, sys.stderr = old_out, old_err

    # open_file_and_validate
    def test_open_file_and_validate_no_errors_file(self):
        with self.captured_output() as (out, err):
            self.ctrl.open_file_and_validate('data/no_errors.csv')
        lines = out.getvalue().splitlines()[-1]
        expected = "data/no_errors.csv Inputted with no errors"
        self.assertEqual(expected, lines)

    def test_open_file_and_validate_errors_file_get_first_message(self):
        with self.captured_output() as (out, err):
            self.ctrl.open_file_and_validate('data/data_02.csv')
        lines = out.getvalue().splitlines()[-2]
        expected = "Records with errors dropped:"
        self.assertEqual(expected, lines)

    # show_graph
    def test_show_graph_no_errors_file(self):
        with self.captured_output() as (out, err):
            self.ctrl.show_graph('data/no_errors.csv', '')
        lines = out.getvalue().splitlines()[-1]
        expected = "data/no_errors.csv opened successfully"
        self.assertEqual(expected, lines)

    def test_show_graph_invalid_file(self):
        # with self.captured_output() as (out, err):
        #     self.ctrl.show_graph('data/xxx.csv', 'input')
        self.assertFalse(self.ctrl.show_graph('data/xxx.csv', 'input'))

    def test_show_graph_valid_file_pie_graph(self):
        self.assertIsNone(self.ctrl.show_graph('data/data_02.csv', "pie"))

    def test_show_graph_valid_file_no_type_graph(self):
        self.assertIsNone(self.ctrl.show_graph('data/data_02.csv', ""))

    # save_data_to_new_file
    def test_save_data_to_new_file_file_does_not_exist(self):
        # delete the existing test file
        filename = "data/saved_file.csv"
        try:
            os.remove(filename)
        except OSError:
            pass

        # create data to ensure it gets past the next step
        self.ctrl._data_list = ["Item1b","Item2","Item3"]
        with self.captured_output() as (out, err):
            self.ctrl.save_data_to_new_file(filename)

        lines = out.getvalue().strip()
        expected = ''
        self.assertEqual(expected, lines)

    def test_save_data_to_new_file_file_exists(self):
        self.ctrl._data_list = ["Item1d", "Item2", "Item3"]
        self.assertFalse(self.ctrl.save_data_to_new_file("data/saved_file.csv"))

    def test_save_data_to_new_file_file_does_not_exists_invalid_extension(self):
        self.ctrl._data_list = ["Item1d", "Item2", "Item3"]
        self.assertFalse(self.ctrl.save_data_to_new_file("data/saved_file.xxx"))


    def test_save_data_to_new_file_no_data_list(self):
        filename = "data/saved_file.csv"
        try:
            os.remove(filename)
        except OSError:
            pass
        with self.captured_output() as (out, err):
            self.ctrl.save_data_to_new_file("data/saved_file.csv")

        lines = out.getvalue().strip()
        expected = "There is no data present." \
                   " Use 'file <filename>' to input data"
        self.assertEqual(expected, lines)

    # show_records
    def test_show_records(self):
        self.ctrl._data_list = ["Item1","Item2","Item3"]
        with self.captured_output() as (out, err):
            self.ctrl.show_records()

        lines = out.getvalue().strip()
        expected = "Item1\nItem2\nItem3"
        self.assertIn(expected, lines)

    # check_valid_file_name
    def test_check_valid_file_name_no_file_name(self):
        self.assertFalse(self.ctrl.check_valid_file_name('', 'input'))

    def test_check_valid_file_name_valid_file_name(self):
        self.assertTrue(self.ctrl.check_valid_file_name
                        ('data/data_employee.db','input'))

    def test_check_valid_file_name_not_valid_file_name_valid_ext(self):
        self.assertFalse(self.ctrl.check_valid_file_name
                        ('data/xxx.db','input'))

    def test_check_valid_file_name_not_valid_file_name_invalid_ext(self):
        self.assertFalse(self.ctrl.check_valid_file_name
                        ('data/data_05.txt','input'))

    # check_file_name_extensions
    def test_check_file_name_extensions_db(self):
        self.assertTrue(self.ctrl.check_file_name_extensions
                        ('data/data_employee.db', 'input'))

    def test_check_file_name_extensions_csv(self):
        self.assertTrue(self.ctrl.check_file_name_extensions
                        ('data/employee.csv', 'input'))

    def test_check_file_name_extensions_txt_input(self):
        self.assertFalse(self.ctrl.check_file_name_extensions
                         ('data/employee.txt', 'input'))

    def test_check_file_name_extensions_txt_output(self):
        self.assertFalse(self.ctrl.check_file_name_extensions
                         ('data/employee.txt', 'output'))

    def test_check_file_name_extensions_db_output(self):
        self.assertTrue(self.ctrl.check_file_name_extensions
                         ('data/employee.db', 'output'))

    # check_file_exists
    def test_check_file_exists_valid_file(self):
            self.assertTrue(self.ctrl.check_file_exists
                             ('data/data_02.csv'))

    def test_check_file_exists_invalid_file(self):
        self.assertFalse(self.ctrl.check_file_exists
                        ('data/xx.csv'))

if __name__ == '__main__':
    unittest.main()
