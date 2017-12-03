# Written By Vaishali

import sys
import os
from controller import Controller
from employee import Employee
from command_view import CommandView
from view_csv_file import CsvFileView
from view_database import DatabaseView
from view_pickle import PickleView
from contextlib import contextmanager
from io import StringIO


import unittest

class CommandViewUnitTests(unittest.TestCase):
    def setUp(self):
        self.cmd_view = CommandView()
        csv_view = CsvFileView()
        pickle_view = PickleView()
        database_view = DatabaseView()
        view_list = [csv_view, database_view, pickle_view]
        self.ctrl = Controller(view_list, self.cmd_view, Employee())
        self.cmd_view.set_controller(self.ctrl)
        pass

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

    # do_read
    def test_do_read_file_does_not_exist(self):
        with self.captured_output() as (out, err):
            self.cmd_view.do_read("data/xxx_csv")
        lines = out.getvalue().strip()
        expected = "File does not exist"
        self.assertIn(expected, lines)

    def test_do_read_no_file_name(self):
        with self.captured_output() as (out, err):
            self.cmd_view.do_read("")
        lines = out.getvalue().strip()
        expected = "Usage: read <file_name>"
        self.assertIn(expected, lines)

    def test_do_read_correct_file_name(self):
        with self.captured_output() as (out, err):
            self.cmd_view.do_read("data/data_05.csv")
        lines = out.getvalue().strip()
        expected = "data/data_05.csv opened successfully"
        self.assertIn(expected, lines)

    def test_do_read_invalid_file_name(self):
        with self.captured_output() as (out, err):
            self.cmd_view.do_read("data/xx.csv")
        lines = out.getvalue().strip()
        expected = "File does not exist"
        self.assertIn(expected, lines)

    # do_show
    def test_do_show_no_file_name(self):
        with self.captured_output() as (out, err):
            self.cmd_view.do_show("")
        lines = out.getvalue().splitlines()[-1]
        expected = "Records shown are from the " \
                   "file inputted using 'read <filename>'"
        self.assertEqual(expected, lines)

    def test_do_show_valid_file_name(self):
        with self.captured_output() as (out, err):
            self.cmd_view.do_show("data/data_02.csv")
        lines = out.getvalue().strip()
        expected = "data/data_02.csv opened successfully\n" \
                   "Records with errors dropped:\n" \
                   "Record 2, DOB : Age does not match DOB\n" \
                   "['A123', 'M', '25', '123', 'Normal', '39', '31-01-1992']"
        self.assertEqual(expected, lines)

    def test_do_show_records_use_do_show(self):
        with self.captured_output() as (out, err):
            self.cmd_view.do_show("data/data_02.csv")
        lines = out.getvalue().strip()
        expected = "data/data_02.csv opened successfully"\
            "\nRecords with errors dropped:"\
            "\nRecord 2, DOB : Age does not match DOB"\
            "\n['A123', 'M', '25', '123', 'Normal', '39', '31-01-1992']"
        self.assertIn(expected, lines)

    def test_do_show_records_use_show_records(self):
        self.cmd_view.do_read("data/data_02.csv")
        with self.captured_output() as (out, err):
            self.ctrl.show_records()
        lines = out.getvalue().strip()
        expected = \
            "['A123', 'M', '25', '123', 'Normal', '39', '31-01-1992']"
        self.assertIn(expected, lines)

    def test_do_show_test_return_value_False(self):
        expected = self.cmd_view.do_show("data/xx.csv")
        self.assertEqual(expected, None)

    # do_graph
    def test_do_graph_no_file_name(self):
        with self.captured_output() as (out, err):
            self.cmd_view.do_graph("")
        lines = out.getvalue().splitlines()[-1]
        expected = "Usage: graph <filename> [args]"
        self.assertEqual(expected, lines)

    def test_do_graph_Invalid_file_name(self):
        with self.captured_output() as (out, err):
            self.cmd_view.do_graph("data/xxx.csv")
        lines = out.getvalue().strip()
        expected = "File does not exist"
        self.assertEqual(expected, lines)

    def test_do_graph_valid_file_name(self):
        with self.captured_output() as (out, err):
            self.cmd_view.do_graph("data/data_02.csv")
        lines = out.getvalue().strip()
        expected = "data/data_02.csv opened successfully"
        self.assertEqual(expected, lines)

    def test_do_graph_valid_file_name_pie_arg(self):
        with self.captured_output() as (out, err):
            self.cmd_view.do_graph("data/data_02.csv pie")
        lines = out.getvalue().strip()
        expected = "data/data_02.csv opened successfully"
        self.assertEqual(expected, lines)

    # do_save
    def test_do_save_no_file_name(self):
        with self.captured_output() as (out, err):
            self.cmd_view.do_save("")
        lines = out.getvalue().splitlines()[-1]
        expected = "Usage: save <file_name>"
        self.assertEqual(expected, lines)

    def test_do_save_no_file_name_return_false(self):
        self.assertFalse(self.cmd_view.do_save(""))

    def test_do_save_no_file_name_return_true(self):
        filename = "data/saved_file.csv"
        try:
            os.remove(filename)
        except OSError:
            pass
        self.assertTrue(self.cmd_view.do_save(filename))

    def test_do_save_to_new_file_name(self):
        self.cmd_view.do_read("data/data_02.csv")
        filename = "data/saved_file.csv"
        try:
            os.remove(filename)
        except OSError:
            pass

        expected = True
        actual = self.cmd_view.do_save(filename)
        self.assertEqual(expected, actual)

    # do_quit
    def test_do_quit_test_string(self):
        with self.captured_output() as (out, err):
            self.cmd_view.do_quit('')
        lines = out.getvalue().strip()
        expected = "Quitting ......."
        self.assertIn(expected, lines)

    def test_do_quit_test_return_value(self):
        expected = self.cmd_view.do_quit('')
        self.assertEqual(expected, True)

if __name__ == '__main__':
    unittest.main(verbosity=2)
