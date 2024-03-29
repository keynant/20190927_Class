from tkinter import *
import time
# place items on self (window)
# IntVar
# StringVar
# grid
# validate?
# listbox ?

class CalculatorWindow:
    def __init__(self, root):
        self.root= root
        root.title("Calculator")
        self.total_value = DoubleVar()
        self.total_value.set(0)
        self.total_label = Label(root,
                                 textvariable=self.total_value,
                                 font=("david", 24))
        self.total_label.pack()

        self.entry = Entry(root, text="0", font=("david", 24))
        self.entry.pack()

        # self.entry.get() -- returns the Entry text value

        self.addBtn = Button(text="Add",font=("david", 24),
                             #command=self.add1)
                             command=lambda: self.total_value.set(self.total_value.get() + float(self.entry.get())))
        self.addBtn.pack()

        self.subBtn = Button(text="Sub",font=("david", 24),
                             command=lambda: self.total_value.set(self.total_value.get() - float(self.entry.get())))
        self.subBtn.pack()

        self.mulBtn = Button(text="Mul",font=("david", 24),
                             command=lambda: self.total_value.set(self.total_value.get() * float(self.entry.get())))
        self.mulBtn.pack()

        self.divBtn = Button(text="Div",font=("david", 24),
                             command=lambda: self.total_value.set(self.total_value.get() / float(self.entry.get())))
        self.divBtn.pack()

        self.CBtn = Button(text="C",font=("david", 24),
                             command=lambda: self.total_value.set(0))
        self.CBtn.pack()

    def add1(self):
        self.total_value.set(self.total_value.get() + 1)

root = Tk()
my_window = CalculatorWindow(root)
root.mainloop()  # blocking
