import tkinter as tk

class CalculatorModel:
    def __init__(self):
        self.expression = ""

    #Metoda sloužící k přidání uživatelského vstupu do výrazu
    def add_to_expression(self, value):
        self.expression += str(value)

    #Vyhodnocení výrazu a aktualizace výsledku
    def evaluate_expression(self):
        try:
            result = eval(self.expression)
            self.expression = str(result)
        except ZeroDivisionError:
            self.expression = "Error: Division by zero"
        except SyntaxError:
            self.expression = "Error: Invalid syntax"
        except Exception:
            self.expression = "Error:" + str(e)