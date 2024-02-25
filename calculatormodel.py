import tkinter as tk

class CalculatorModel:
    def __init__(self):
        self.expression = ""

    def add_to_expression(self, value):
        self.expression += str(value)