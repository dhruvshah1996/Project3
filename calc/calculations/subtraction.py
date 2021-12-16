"""Subtraction Class"""
from calc.calculations.calculation import Calculation

class Subtraction(Calculation):
    """subtraction calculation object"""
    def get_result(self):
        """get the subtraction results"""

        sub1 = enumerate(self.values)
        for i, value in (sub1):
            if i != 0:
                difference_of_values = difference_of_values - value
            else:
                difference_of_values = value

        return difference_of_values