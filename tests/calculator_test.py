"""Testing the Calculator"""
import pytest
from calc.calculator import Calculator
from calc.history.calculations import Calculations
from calc.calculations.addition import Addition
from calc.calculations.multiplication import Multiplication
from calc.calculations.subtraction import Subtraction

@pytest.fixture
def clear_history_fixture():
    """define a function that will run each time you pass it to a test, it is called a fixture"""
    # pylint: disable=redefined-outer-name
    Calculations.clear_history()
#You have to add the fixture function as a parameter to the test that you want to use it with
def test_calculator_add_static(clear_history_fixture):
    """testing that our calculator has a static method for addition"""
    # pylint: disable=unused-argument,redefined-outer-name
    #using Tuple instead of args because we can pack as much data as we need into the tuple
    my_tuple = (1.0,2.0,5.0)
    assert isinstance(Calculator.add_numbers(my_tuple), Addition)
    assert Calculator.get_last_result_value() == 8.0
def test_calculator_subtract_static(clear_history_fixture):
    """Testing the subtract method of the calc"""
    # pylint: disable=unused-argument,redefined-outer-name
    #using Tuple instead of args because we can pack as much data as we need into the tuple
    my_tuple = (1.0,2.0,3.0)
    #creating the calculation result object
    calculation_result_object = Calculator.subtract_numbers(my_tuple)
    #testing the instance
    assert isinstance(calculation_result_object, Subtraction)
    #testing the last result of the calculation
    assert Calculator.get_last_result_value() == -4.0
    #testing that the result object performs the calculation
    assert calculation_result_object.get_result() == -4.0

def test_calculator_multiply_static(clear_history_fixture):
    """Testing the subtract method of the calc"""
    # pylint: disable=unused-argument,redefined-outer-name
    #using Tuple instead of args because we can pack as much data as we need into the tuple
    my_tuple = (1.0,2.0,3.0)
    assert isinstance(Calculator.multiply_numbers(my_tuple), Multiplication)
    assert Calculator.get_last_result_value() == 6.0
