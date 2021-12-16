import pandas as pd

from app.controllers.controller import ControllerBase
from calc.calculator import Calculator
from flask import render_template, request, flash, redirect, url_for


class CalculatorController(ControllerBase):
    @staticmethod
    def post():
        if request.form['value1'] == '' or request.form['value2'] == '':
            error = 'You have to enter a value for both fields please'
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

            d = {"value1": value1, "value2": value2, "operation": operation, "result": result}
            df = pd.DataFrame(d)
            df.to_csv("results.csv", index=None, na_rep="na", mode='a')

            return render_template('result.html', value1=value1, value2=value2, operation=operation, result=result)
        return render_template('calculator2.html', error=error)
    @staticmethod
    def get():
        return render_template('calculator2.html')




