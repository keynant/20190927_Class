from tkinter import *
from datetime import *

class CalculatorWindow:
    def __init__(self, root):
        self.root= root
        root.title("Calculator")
        self.total_value = IntVar()
        self.total_value.set(0)
        self.total_label = Label(root,
                                 textvariable=self.total_value,
                                 font=("david", 72))
        self.total_label.pack()
        self.addBtn1 = Button(text="Add",
                             command=lambda: self.total_value.set(self.total_value.get() + 1))
        self.addBtn1.pack()
        self.addBtn2 = Button(text="Subtract",
                              command=lambda: self.total_value.set(self.total_value.get() - 1))
        self.addBtn2.pack()
        self.addBtn3 = Button(text="Reset",
                              command=lambda: self.total_value.set(0))
        self.addBtn3.pack()

        self.dateLabel = StringVar()
        self.dateLabel.set("Hello")
        self.total_label2 = Label(root,
                                 textvariable=self.dateLabel,
                                 font=("david", 72))
        self.total_label2.pack()
        self.addBtn4 = Button(text="Show Date",
                              command=lambda: self.dateLabel.set(date.today()))
        self.addBtn4.pack()


root = Tk()
my_window = CalculatorWindow(root)
root.mainloop()

# targil;
# add button which decrease 1
# add button which sets the value back to 0
# with lambda?
