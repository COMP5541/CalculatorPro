__author__ = "The CalculatorPro Inc."
__copyright__ = "Copyright 2018, CalculatorPro"
__credits__ = ["Team A"]
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "Beranrdo Sandi"
__email__ = "B_SANDI@encs.concordia.ca"
__status__ = "Release v1.0"


from tkinter import *

#Initialize GUI

class GUI:

    def __init__(self, master, controller):
        self.master = master
        self.master.title('ETERNITY')
        self.master.geometry()
        self.entry = Entry(master, font = ("Times", 15, 'bold'))
        self.entry.grid(row=0, column=0, columnspan=10, sticky = W+E)
        self.entry.focus_set()
        self.controller = controller


        # Creating Buttons

        # Number Pad
        Button(master, text="7", width=3, command=lambda: self.controller.inputVal(7), font=("times", 15)).grid(row=1, column=0)
        Button(master, text="4", width=3, command=lambda: self.controller.inputVal(4), font=("times", 15)).grid(row=2, column=0)
        Button(master, text="1", width=3, command=lambda: self.controller.inputVal(1), font=("times", 15)).grid(row=3, column=0)
        Button(master, text="0", width=3, command=lambda: self.controller.inputVal(0), font=("times", 15)).grid(row=4, column=0)

        Button(master, text="8", width=3, command=lambda: self.controller.inputVal(8), font=("times", 15)).grid(row=1, column=1)
        Button(master, text="5", width=3, command=lambda: self.controller.inputVal(5), font=("times", 15)).grid(row=2, column=1)
        Button(master, text="2", width=3, command=lambda: self.controller.inputVal(2), font=("times", 15)).grid(row=3, column=1)
        Button(master, text=".", width=3, command=lambda: self.controller.inputOperator('.'), font=("times", 15)).grid(row=4, column=1)

        Button(master, text="9", width=3, command=lambda: self.controller.inputVal(9), font=("times", 15)).grid(row=1, column=2)
        Button(master, text="6", width=3, command=lambda: self.controller.inputVal(6), font=("times", 15)).grid(row=2, column=2)
        Button(master, text="3", width=3, command=lambda: self.controller.inputVal(3), font=("times", 15)).grid(row=3, column=2)
        Button(master, text="=", width=3, command=lambda: self.controller.calculate(), font=("times", 15), foreground = "red").grid(row=4, column=2)


            # Functions
        Button(master, text='C', width=3, command=lambda: self.controller.deleteOne(), font=("times", 15), foreground="red").grid(row=1, column=4)
        Button(master, text="*", width=3, command=lambda: self.controller.inputOperator('*'), font=("times", 15)).grid(row=2, column=4)
        Button(master, text="+", width=3, command=lambda: self.controller.inputOperator('+'), font=("times", 15)).grid(row=3,column=4)
        Button(master, text="(", width=3, command=lambda: self.controller.inputOperator('('), font=("times", 15)).grid(row=4,column=4)

        Button(master, text='AC', width=3, command=lambda: self.controller.clearAll(), font=("times", 15),foreground="red").grid(row=1, column=5)
        Button(master, text="/", width=3, command=lambda: self.controller.inputOperator('/'), font=("times", 15)).grid(row=2,column=5)
        Button(master, text="-", width=3, command=lambda: self.controller.inputOperator('-'), font=("times", 15)).grid(row=3,column=5)
        Button(master, text=")", width=3, command=lambda: self.controller.inputOperator(')'), font=("times", 15)).grid(row=4,column=5)

        Button(master, text="√", width=3, command=lambda: self.controller.square(), font=("times", 15)).grid(row=1, column=6)
        Button(master, text="ln(x)", width=3, command=lambda: self.controller.ln(), font=("times", 15)).grid(row=2, column=6)
        Button(master, text="sin", width=3, command=lambda: self.controller.sine(), font=("times", 15)).grid(row=3, column=6)
        Button(master, text="e^(x)", width=3, command=lambda: self.controller.exFunc(), font=("times", 15)).grid(row=4, column=6)

        Button(master, text="10^x", width=3, command=lambda: self.controller.tenToPower(), font=("times", 15)).grid(row=1, column=7)


    # def get(self):
    #     return eval(self.entry.get())


