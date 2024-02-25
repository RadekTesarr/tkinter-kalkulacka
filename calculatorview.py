import tkinter as tk

class CalculatorView:
    def __int__(self, root, controller):
        self.controller == controller

        self.entry = tk.Entry(root, width=20, font=("Arial", 14))
        self.entry.grid(row=0, column=0, columnspan=5, padx=10, pady=10)

        buttons = [
            {"text": "7", "row":1, "col":0},
            {"text": "8", "row":1, "col":1},
            {"text": "9", "row":1, "col":2},
            {"text": "/", "row":1, "col":3},
            {"text": "4", "row":2, "col":0},
            {"text": "5", "row":2, "col":1},
            {"text": "6", "row":2, "col":2},
            {"text": "*", "row":2, "col":3},
            {"text": "1", "row":3, "col":0},
            {"text": "2", "row":3, "col":1},
            {"text": "3", "row":3, "col":2},
            {"text": "-", "row":3, "col":3},
            {"text": "0", "row":4, "col":0},
            {"text": ".", "row":4, "col":1},
            {"text": "=", "row":4, "col":2},
            {"text": "+", "row":4, "col":3},
            {"text": "C", "row":1, "col":4, "bg":"#FF9500"},
            {"text": "AC", "row":2, "col":4, "bg":"#FF3B30"},
        ]