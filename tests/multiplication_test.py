"""Testing Addition"""
import logging
import pandas as pd
import os
from calc import log
from calc.calculations.multiplication import Multiplication


dirname = os.path.dirname(os.path.realpath(__file__))

def test_calculation_multiplication():
    """testing addition method with csv inputs"""
    fileName = '/Users/dhruvshah/PycharmProjects/calc2/tests/CSVFiles/Multiplication.csv'
    inputFile = os.path.join(fileName)
    df = pd.read_csv("CSVFiles/Multiplication.csv")
    print(df.head(10))
    for x, y in df.iterrows():
        mul = (y.Value_1, y.Value_2)
        record = x
        multiplication = Multiplication.create(mul)
        log.logging_data(inputFile, "multiplication", record)
        logging.debug("This is the result")
        assert multiplication.get_result() == df['Result'][x]