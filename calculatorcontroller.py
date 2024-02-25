import tkinter as tk

class CalculatorController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    #Zpracování výrazu v modelu
    def process_input(self, value):
        if value == "=":
            self.model.evaluate_expression()
        else:
            self.model.add_to_expression(value)
        self.update_view()

    #Odstranění posledního znaku
    def clear_input(self):
        self.model.expression = self.model.expression[:-1]
        self.update_view()

    #Smazání vstupu
    def clear_all(self):
        self.model.expression = ""
        self.update_view()

    def update_view(self):
        self.view.entry.delete(0, tk.END)
        self.view.entry.insert(0, self.model.expression)