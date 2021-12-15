"""A simple flask web app"""
from flask import Flask
from app.controllers.index_controller import IndexController, pylintController, AAAtestingController
from app.controllers.index_controller import SOLIDController, OOPController
from app.controllers.calculator_controller import CalculatorController

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route("/", methods=['GET'])
def index_get():
    return IndexController.get()

@app.route("/calculator", methods=['GET'])
def calculator_get():
    return CalculatorController.get()

@app.route("/calculator", methods=['POST'])
def calculator_post():
    return CalculatorController.post()

@app.route("/pylint", methods=['GET'])
def pylint_get():
    return pylintController.get()

@app.route("/AAATest", methods=['GET'])
def AAA_get():
    return AAAtestingController.get()

@app.route("/OOP", methods=['GET'])
def OOP_get():
    return OOPController.get()

@app.route("/SOLID", methods=['GET'])
def SOLID_get():
    return SOLIDController.get()