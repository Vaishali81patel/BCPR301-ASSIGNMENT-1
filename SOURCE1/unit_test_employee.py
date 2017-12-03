# written by Vaishali
"""
Does unit tests for the command view
"""

import unittest
from employee import Employee
import sys
from contextlib import contextmanager
from io import StringIO


class EmployeeUnitTests(unittest.TestCase):
    def setUp(self):
        self.employee = Employee()
		# a list of two valid employee files

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

   
	# employee_info
    def test_employee_info_no_header(self):
        employees_list_no_header = [
            ['A123', 'M', '25', '123', 'Normal', '39', '31-01-1992'],
            ['T123', 'M', '20', '654', 'Normal', '56', '16/10/1996']]
        result = self.employee.employee_info(employees_list_no_header)
        # remove the header
        self.assertEqual(employees_list_no_header, result[0])

    def test_employee_info_with_header(self):
        employees_list_with_header = [
            ['empid', 'gender', 'age', 'sales', 'bmi', 'salary', 'dob'],
            ['A123', 'M', '25', '123', 'Normal', '39', '31-01-1992'],
            ['T123', 'M', '20', '654', 'Normal', '56', '16/10/1996']]
        result = self.employee.employee_info(employees_list_with_header)
        # remove the header
        employees_list_with_header.pop(0)
        self.assertEqual(employees_list_with_header, result[0])
        self.assertEqual([], result[1])

    def test_employee_info_same_empid(self):
        employees_list_duplicate_id = [
            ['A123', 'M', '25', '123', 'Normal', '39', '31-01-1992'],
            ['A123', 'M', '20', '654', 'Normal', '56', '16/10/1996']]
        result = self.employee.employee_info(employees_list_duplicate_id)
        # remove duplicate record
        employees_list_duplicate_id.pop(1)
        self.assertEqual(employees_list_duplicate_id, result[0])
        self.assertEqual([['Record 2', 'EmpID not unique']], result[1])

    def test_employee_info_invalid_record(self):
        employees_list_invalid_record = [
            ['A123', 'M', '25', '123', 'Normal', '39', '31-01-1992'],
            ['T123', 'X', '20', '654', 'Normal', '56', '16/10/1996']]
        result = self.employee.employee_info(employees_list_invalid_record)
        # remove invalid record
        employees_list_invalid_record.pop(1)
        self.assertEqual(employees_list_invalid_record, result[0])
        # error list
        self.assertEqual([['Record 2', 'Gender : Not M or F']], result[1])

    # create tests for new extracted methods
    # create_string_of_only_lowercase_alphabet_characters

    def test_create_only_lowercase_alphabet_characters_input_only_alpha(self):
        input_string = "abc"
        result = \
            self.employee.create_string_of_only_lowercase_alphabet_characters(
                                                                input_string)
        self.assertEqual(input_string, result)

    def test_create_only_lowercase_alphabet_characters_input_upper_alpha(self):
        input_string = "ABC"
        result = \
            self.employee.create_string_of_only_lowercase_alphabet_characters(
                input_string)
        self.assertEqual("abc", result)

    def test_create_only_lowercase_alphabet_characters_input_mixed(self):
        input_string = "a_B#c"
        result = \
            self.employee.create_string_of_only_lowercase_alphabet_characters(
                input_string)
        self.assertEqual("abc", result)

    # extract_list_from_two_deep_list
    def test_extract_list_from_list_of_lists(self):
        list_one = ["1a","2a","3a"]
        list_two = ["1b","2b","3b"]
        input_two_deep_list = [list_one, list_two]
        result = self.employee.extract_list_from_list_of_lists(
                                                        input_two_deep_list,0)
        self.assertEqual(list_one, result)

if __name__ == '__main__':
    unittest.main()
