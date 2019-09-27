from tkinter import *
import time
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
        self.subBtn = Button(text="Subtract",
                             command=lambda: self.total_value.set(self.total_value.get() - 1))
        self.subBtn.pack()
        self.rstBtn = Button(text="Reset",
                             command=lambda: self.total_value.set(0))
        self.rstBtn.pack()

        self.dateLabel = StringVar()
        self.dateLabel.set("Hello")
        self.total_label2 = Label(root,
                                 textvariable=self.dateLabel,
                                 font=("david", 72))
        self.total_label2.pack()
        self.updateTimeBtn = Button(text="Show Date",
                                    command=lambda: self.dateLabel.set(time.ctime()))
        self.updateTimeBtn.pack()



root = Tk()
my_window = CalculatorWindow(root)
root.mainloop()
