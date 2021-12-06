"""Testing Addition"""
import pandas as pd
import os
import logging
from calc import log
from calc.calculations.division import Division

dirname = os.path.dirname(os.path.realpath(__file__))

def test_calculation_division():
    """testing division method with csv inputs"""
    fileName = 'CSVFiles/Subtraction.csv'
    inputFile = os.path.join(fileName)
    df = pd.read_csv("CSVFiles/Division.csv")
    print(df.head(3))
    for x, y in df.iterrows():
        div = (y.Value_1, y.Value_2)
        record = x
        division = Division.create(div)
        log.logging_data(inputFile, "division", record)
        try:
            assert division.get_result() == df['Result'][x]
        except ZeroDivisionError:
            print("Cannot divide by zero")
