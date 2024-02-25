import tkinter as tk
from calculatormodel import CalculatorModel
from calculatorview import CalculatorView
from calculatorcontroller import CalculatorController

if __name__ == "__main__":
    root = tk.Tk()
    root.configure(pady=15, padx=15)
    root.title("Calculator")

    model = CalculatorModel()
    view = CalculatorView(root, None)
    controller = CalculatorController(model, view)
    view.controller = controller

    root.mainloop()