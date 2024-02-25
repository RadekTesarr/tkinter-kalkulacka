import tkinter as tk

class CalculatorView:
    def __int__(self, root, controller):
        self.controller == controller

        #Vstupní widget entry
        self.entry = tk.Entry(root, width=20, font=("Arial", 14))
        #Pozicování widgetů
        self.entry.grid(row=0, column=0, columnspan=5, padx=10, pady=10)

        #Tlačítka kalkulačky
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

        #Usazení tlačítek
        for button in buttons:
            btn = tk.Button(root, text=button["text"], width=5, height=2, font=("Arial", 12))
            btn.grid(row=button["row"], column=button["col"], padx=5, pady=5)

        #Změna barvy
        if "bg" in button:
            btn.configure(bg=button["bg"], fg="white")
            btn.bind("<Button-1>", self.handle_button_click)

        def handle_button_click(self, event):
            value = event.widget.cget("text")
            if value == "C":
                self.controller.clear_input()
            elif value == "AC":
                self.controller.clear_all()
            else:
                self.controller.process_input(value)