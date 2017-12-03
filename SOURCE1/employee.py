# written by Vaishali

from validate_age import Age
from validate_emp_id import EmpID
from validate_gender import Gender
from validate_bmi import BMI
from validate_sales import Sales
from validate_salary import Salary
from validate_dob import DOB
from data_csv import DataCSV
from model import Model
import re


class Employee(Model):
    _employee_objects = []

    def __init__(self):
        self._employee_objects.append(EmpID)
        self._employee_objects.append(Gender)
        self._employee_objects.append(Age)
        self._employee_objects.append(Sales)
        self._employee_objects.append(BMI)
        self._employee_objects.append(Salary)
        self._employee_objects.append(DOB)

    def employee_info(self, employees_list):
        """
        Iterates through the employees_list, validating fields
        :param employees_list:
        :return: valid_employees, error_list
        """
        error_list = []
        valid_employees = []
        record_num = 0
        row_num = 0
        stored_emp_ids = []
        id_field_header = "empid"

        for row in employees_list:
            record_error_list = []
            employee_data = self.extract_list_from_list_of_lists(
                                                    employees_list, row_num)
            emp_id_field = employee_data[0]
            row_num += 1  # increase to get next row next time through
            id_field = self.create_string_of_only_lowercase_alphabet_characters(
                                                                emp_id_field)
            if id_field != id_field_header:
                record_num += 1
                        # used to display record number if there is an error
                found_error = self.check_unique_emp_id(emp_id_field,
                                            stored_emp_ids, record_error_list)
                if not found_error:
                    found_error = self.validate_record_info(employee_data,
                                                        record_error_list)
                if found_error:
                    record_error_list.insert(0, "Record " + str(record_num))
                    error_list.append(record_error_list)
                else:
                    valid_employees.append(row)

        return valid_employees, error_list

    @staticmethod
    def check_unique_emp_id(this_emp_id, stored_emp_ids, record_error_list):
        found_id_error = False
        stored_emp_ids.append(this_emp_id)
        for emp_id in stored_emp_ids[:-1]:
            if this_emp_id == emp_id:
                found_id_error = True
                record_error_list.append("EmpID not unique")
        return found_id_error

    def validate_record_info(self, employee_data, record_error_list):
        found_record_error = False
        for i in range(len(employee_data)):
            # put the value into a data object of the appropriate type
            x = self._employee_objects[i](employee_data[i])
            result = x.validate()
            if (self._employee_objects[i] == DOB) & (result == "Valid"):
                result = x.check_age_against_date(employee_data[2])
            if result != "Valid":
                found_record_error = True
                record_error_list.append(self._employee_objects[i].
                                         __name__ + " : " + result)
        return found_record_error

    @staticmethod
    def create_string_of_only_lowercase_alphabet_characters(input_string):
        temp_string = re.sub('[^0-9a-zA-Z]+', '', input_string)
        output_string = temp_string.lower()
        return output_string

    @staticmethod
    def extract_list_from_list_of_lists(list, record_num):
        data_csv = DataCSV(list)
        return data_csv.unpack_data(record_num)
