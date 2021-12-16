from app.controllers.controller import ControllerBase
from calc.calculator import Calculator
from flask import render_template, request, flash, redirect, url_for
import os.path
import pandas as pd

class CalculatorController(ControllerBase):
    @staticmethod
    def post():
        if request.form['value1'] == '' or request.form['value2'] == '':
            error = 'You must enter a value for value 1 and or value 2'
        else:
            flash('You successfully calculated')
            # get the values out of the form
            value1 = request.form['value1']
            value2 = request.form['value2']
            operation = request.form['operation']
            # make the tuple
            my_tuple = (value1, value2)
            # this will call the correct operation
            getattr(Calculator, operation)(my_tuple)
            result = str(Calculator.get_last_result_value())

            if not os.path.exists('results.csv'):
                f = open("results.csv", "w")
                f.write(f"value1,value2,operation,result\n")
                f.close()

            f1 = open("results.csv", "a")
            f1.write(f"{value1},{value2},{operation},{result}\n")
            f1.close()

            df = pd.read_csv("results.csv")
            print(df)

            items = []
            for row in df.iterrows():
                items.append(row)

            return render_template('result.html', items=items)
        return render_template('calculator2.html', error=error)
    @staticmethod
    def get():
        return render_template('calculator2.html')
