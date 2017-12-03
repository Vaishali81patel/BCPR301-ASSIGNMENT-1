# Written By Vaishali
#
"""
Unit Testing with Python

"""

from unit_test_command import *
from unit_test_controller import *
from unit_test_employee import *

import unittest
import doctest

def unit_suite():
    theSuite = unittest.TestSuite()
    theSuite.addTest(unittest.makeSuite(CommandViewUnitTests))
    theSuite.addTest(unittest.makeSuite(ControllerUnitTests))
    theSuite.addTest(unittest.makeSuite(EmployeeUnitTests))
    return theSuite


if __name__ == '__main__':
    runner_unit = unittest.TextTestRunner(verbosity=2)
    test_suite = unit_suite()
    runner_unit.run(test_suite)
