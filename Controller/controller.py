__author__ = "The CalculatorPro Inc."
__copyright__ = "Copyright 2018, CalculatorPro"
__credits__ = ["Team A"]
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "Beranrdo Sandi"
__email__ = "B_SANDI@encs.concordia.ca"
__status__ = "Release v1.0"

#import parser
from Model import funEx, ln, sin, squareroot, tentopowerx
from tkinter import *
from View.view import GUI


class Controller:
    def __init__(self):
        self.root = Tk()
        self.view = GUI(self.root, self)

    def run(self):
        self.root.mainloop()


    def getEntry(self):
        return eval(self.view.entry.get())

    def clearEntry(self):
        self.view.entry.delete(0, END)

    def writeEntry(self,result):
        self.view.entry.insert(0, result)

    def clearAll(self):
        self.view.entry.delete(0, END)

    def deleteOne(self):
        self.txt = self.view.entry.get()[:-1]
        self.view.entry.delete(0, END)
        self.view.entry.insert(0, self.txt)

    def calculate(self):

        try:
            result = self.getEntry()
            self.clearAll()
            self.writeEntry(result)
        except Exception:
            self.clearAll()
            self.view.entry.insert(0, "Error!")



    def inputVal(self, argi):
        self.view.entry.insert(END, argi)

    def inputOperator(self, operator):
        self.view.entry.insert(END, operator)

                # Functions

        # Squareroot function
    def square(self):
        value = self.getEntry()
        self.clearEntry()
        result = squareroot.squareroot(value)
        self.writeEntry(result)


        # Natural Logarithm function
    def ln(self):
        value = self.getEntry()
        self.clearEntry()
        result = ln.loge(value)
        self.writeEntry(result)

        # Ten to the power function
    def tenToPower(self):
        value = self.getEntry()
        self.clearEntry()
        result = tentopowerx.tentopowerx(value)
        self.writeEntry(result)



        # e to the power function
    def exFunc(self):
        value = self.getEntry()
        self.clearEntry()
        result = funEx.fun_ex(value)
        self.writeEntry(result)


        # Sine  function
    def sine(self):
        value = self.getEntry()
        self.clearEntry()
        result = sin.sin(value)
        self.writeEntry(result)



Controller().run()