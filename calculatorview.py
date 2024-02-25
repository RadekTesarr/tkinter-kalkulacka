import tkinter as tk

class CalculatorView:
    def __int__(self, root, controller):
        self.controller == controller

        self.entry = tk.Entry(root, width=20, font=("Arial", 14))
        self.entry.grid(row=0, column=0, columnspan=5, padx=10, pady=10)

