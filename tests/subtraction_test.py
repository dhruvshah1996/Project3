"""Testing Subtraction"""
import pandas as pd
from calc import log
import logging
import os
from calc.calculations.subtraction import Subtraction

dirname = os.path.dirname(os.path.realpath(__file__))

def test_calculation_subtraction():
    """testing that our calculator has a static method for addition"""
    fileName = 'CSVFiles/Subtraction.csv'
    inputFile = os.path.join(fileName)
    df = pd.read_csv("CSVFiles/Subtraction.csv")
    print(df.head(5))
    for x, y in df.iterrows():
        sub = (y.Value_1, y.Value_2)
        record = x
        subtraction = Subtraction.create(sub)
        log.logging_data(inputFile, "subtraction", record)
        logging.debug("This is the result")
        assert subtraction.get_result() == df['Result'][x]
