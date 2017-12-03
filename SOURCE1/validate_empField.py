# Created by Vaishali

import re
from validate_field import ValidateField
from validate_age_validate import AgeValidate
from datetime import date
from dateutil.relativedelta import relativedelta


# Validate Employee_DOB type
class DOB(ValidateField, AgeValidate):
    __correctDate = None
    __date = None
    __date_field = ''

# Validate Employee DOB and change
    def validate(self):
        # if DOB is in dd/mm/yy convert to dd-mm-yy
        self._date_field = self._field.replace('/', '-')
        if re.match('^[0-9]{1,2}-[0-9]{1,2}-[0-9]{4}$',
                    self._date_field) is None:
            return 'DOB is not correct format'

        self.__check_date()

        if self.__correctDate is True:
            return self._valid
        else:
            return 'DOB is not a legal date'

# Validate Employee DOB format
    def __check_date(self):
        date_fields = self._date_field.split('-')

        try:
            self.__date = date(int(date_fields[2]),
                               int(date_fields[1]), int(date_fields[0]))
            self.__correctDate = True
        except ValueError:
            self.__correctDate = False

# Validate Employee DOB against Employee AGE
    def check_age_against_date(self, age):
        self._date_field = self._field.replace('/', '-')
        today = date.today()
        date_fields = self._date_field.split('-')
        self.__date = date(int(date_fields[2]), int(date_fields[1]), int(date_fields[0]))
        rd = relativedelta(today, self.__date)
        if rd.years == int(age):
            return self._valid
        else:
            return 'Age does not match DOB'
	
# Validate Employee ID type 
    def validate(self):
        if re.match('^[A-Z][0-9]{3}$', self._field) is not None:
            return self._valid
        else:
            return 'Employee ID must be of format "X000"'

# Validate Employee Gender type
    def validate(self):
        if re.match('^(M|F)$', self._field) is not None:
            return self._valid
        else:
            return 'Not M or F'

# Validate Employee Salary type
    def validate(self):
        if re.match('^[0-9]{2,3}$', self._field) is not None:
            return self._valid
        else:
            return 'Salary must be 2 or 3 numbers'

# Validate Employee Sales type
    def validate(self):
        # PC corrected to {3} not {2,3} 22-03-17
        if re.match('^[0-9]{3}$', self._field) is not None:
            return self._valid
        else:
            return 'Sales must be 3 numbers'

# Validate Employee BMI type
    def validate(self):
        if re.match('^(Normal|Overweight|Obesity|Underweight)$', self._field) is not None:
            return self._valid
        else:
            return 'BMI not a valid option'

			
