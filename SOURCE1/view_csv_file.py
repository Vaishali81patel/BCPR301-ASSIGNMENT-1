# written by Vaishali
"""
input and output of a csv file
"""

from view import View
import csv


class CsvFileView(View):
    @staticmethod
    def get_input(file_name):
        """
        Reads the file and returns it's contents as a list
        """
        read_csv = []
        try:
            with open(file_name, newline='') as incsv:
                # the csv file is converted to lists of lists
                # csv.reader does not retain information once the file is closed
                # fields are placed into list as strings
                read_csv = list(csv.reader(incsv, delimiter=','))
        except Exception as e:
            print(e)
            return False
        else:
            print(file_name, "opened successfully")
        return read_csv


    @staticmethod
    def save_data_to_new(file_name, data_list):
        """
        Saves the data from <data_list> into a new csv file named <file_name>
        """
        with open(file_name, "a") as outcsv:
            writer = csv.writer(outcsv, delimiter=',')
            # write header line to csv
            writer.writerow(['emp_id', 'gender', 'age',
                             'sales', 'bmi', 'salary', 'dob'])
            for line in data_list:
                # write line to csv
                writer.writerows([line, ])
