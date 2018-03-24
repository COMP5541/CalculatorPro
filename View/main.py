__author__ = "The CalculatorPro Inc."
__copyright__ = "Copyright 2018, CalculatorPro"
__credits__ = ['Team A']
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "Team A"
__email__ = "TeamA@mail.concordia.ca"
__status__ = "Release v1.0"

from CommonAssets.main import Button as btn
from CommonAssets.main import DESIRE_GEOMETRY
from CommonAssets.main import TITLE

from tkinter import Button
from tkinter import END
from tkinter import Entry

class CalculatorGUI:

    def __init__(self, master, controller):

        self.master = master
        self.master.title(TITLE)
        self.master.geometry(DESIRE_GEOMETRY)
        self.master.resizable(width=False, height=False)  # window resizable
        self.controller = controller
        self.entry = Entry(master)
        self.entry.grid(row=0, column=0, columnspan=6)
        self.entry.focus_set()

        #UI desing
        offsetRow=0
        row1=1
        row2=2
        row3=3
        row4=4

        offsetColumn=0
        column0=0 + offsetColumn
        column1=1 + offsetColumn
        column2=2 + offsetColumn
        column3=3 + offsetColumn
        column4=4 + offsetColumn
        column5=5 + offsetColumn

        Button(self.master, text="7", width=3, command=lambda: self.inputVal(7)).grid(row=1, column=column0)
        Button(self.master, text="4", width=3, command=lambda: self.inputVal(4)).grid(row=2, column=column0)
        Button(self.master, text="1", width=3, command=lambda: self.inputVal(1)).grid(row=3, column=column0)
        Button(self.master, text="8", width=3, command=lambda: self.inputVal(8)).grid(row=1, column=column1)
        Button(self.master, text="5", width=3, command=lambda: self.inputVal(5)).grid(row=2, column=column1)
        Button(self.master, text="2", width=3, command=lambda: self.inputVal(2)).grid(row=3, column=column1)
        Button(self.master, text="0", width=3, command=lambda: self.inputVal(0)).grid(row=4, column=column1)
        Button(self.master, text="9", width=3, command=lambda: self.inputVal(9)).grid(row=1, column=column2)
        Button(self.master, text="6", width=3, command=lambda: self.inputVal(6)).grid(row=2, column=column2)
        Button(self.master, text="3", width=3, command=lambda: self.inputVal(3)).grid(row=3, column=column2)

        # Behavior Functions
        Button(self.master, text='AC', width=3, command=lambda: self.clearAll()).grid(row=1, column=column3)
        Button(self.master, text='C',  width=3, command=lambda: self.deleteOne()).grid(row=2, column=column3)
        Button(self.master, text='-/+', width=3, command=lambda: self.controller.buttonevent(btn.minusplus)).grid(row=4, column=column5)

        # MAth Functions
        Button(master, text="sin",   width=3, command=lambda: self.controller.buttonevent(btn.sin)).grid(row=1, column=column5)
        Button(master, text="e^(x)", width=3, command=lambda: self.controller.buttonevent(btn.exp)).grid(row=2, column=column5)
        Button(master, text="10^x",  width=3, command=lambda: self.controller.buttonevent(btn.tenPowx)).grid(row=3, column=column5)
        Button(master, text="√",     width=3, command=lambda: self.controller.buttonevent(btn.sqr)).grid(row=3, column=column3)
        Button(master, text="ln(x)", width=3, command=lambda: self.controller.buttonevent(btn.ln)).grid(row=4, column=column3)

    def clearAll(self):
        self.entry.delete(0, END)

    def deleteOne(self):
        self.txt = self.entry.get()[:-1]
        self.entry.delete(0, END)
        self.entry.insert(0, self.txt)

    def inputVal(self, argi):
        self.entry.insert(END, argi)

if __name__ == '__main__':
    pass