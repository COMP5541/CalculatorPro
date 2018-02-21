__author__ = "The CalculatorPro Inc."
__copyright__ = "Copyright 2018, CalculatorPro"
__credits__ = ["Team A"]
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "Beranrdo Sandi"
__email__ = "B_SANDI@encs.concordia.ca"
__status__ = "Release v1.0"


from tkinter import *

from calculatorFunctions.squareroot import squareroot
from calculatorFunctions.log import ln


class calculator:


    def clearAll(self):
        self.e.delete(0, END)

    def deleteOne(self):
        self.txt = self.e.get()[:-1]
        self.e.delete(0, END)
        self.e.insert(0, self.txt)

    def inputVal(self, argi):
        self.e.insert(END, argi)


    # Functions

    def squareroot(self):
        self.value = eval(self.e.get())

        self.sqrtval = squareroot.squareroot(self.value)
        self.e.delete(0, END)
        self.e.insert(0, self.sqrtval)



    def ln(self):
        self.value = eval(self.e.get())

        self.sqrtval = ln.loge(self.value)
        self.e.delete(0, END)
        self.e.insert(0, self.sqrtval)



    def __init__(self, master):
        master.title('CalulatorPro')
        master.geometry()
        self.e = Entry(master)
        self.e.grid(row=0, column=0, columnspan=6 )
        self.e.focus_set()




        # Creating Buttons
        Button(master, text='AC', width=3, command=lambda: self.clearAll()).grid(row=1, column=4)
        Button(master, text='C', width=3, command=lambda: self.deleteOne()).grid(row=2, column=4)
        Button(master, text="9", width=3, command=lambda: self.inputVal(9)).grid(row=1, column=2)
        Button(master, text="8", width=3, command=lambda: self.inputVal(8)).grid(row=1, column=1)
        Button(master, text="7", width=3, command=lambda: self.inputVal(7)).grid(row=1, column=0)
        Button(master, text="6", width=3, command=lambda: self.inputVal(6)).grid(row=2, column=2)
        Button(master, text="5", width=3, command=lambda: self.inputVal(5)).grid(row=2, column=1)
        Button(master, text="4", width=3, command=lambda: self.inputVal(4)).grid(row=2, column=0)
        Button(master, text="3", width=3, command=lambda: self.inputVal(3)).grid(row=3, column=2)
        Button(master, text="2", width=3, command=lambda: self.inputVal(2)).grid(row=3, column=1)
        Button(master, text="1", width=3, command=lambda: self.inputVal(1)).grid(row=3, column=0)
        Button(master, text="0", width=3, command=lambda: self.inputVal(0)).grid(row=4, column=0)
        Button(master, text="√", width=3, command=lambda: self.squareroot()).grid(row=3, column=4)
        Button(master, text="ln", width=3, command=lambda: self.ln()).grid(row=4, column=4)



# Main
root = Tk()
object = calculator(root)  # object instantiated
root.mainloop()