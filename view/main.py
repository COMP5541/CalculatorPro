__author__ = "The CalculatorPro Inc."
__copyright__ = "Copyright 2018, CalculatorPro"
__credits__ = ['Team A']
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "Team A"
__email__ = "TeamA@mail.concordia.ca"
__status__ = "Release v1.0"

from commonAssets.main import Button as btn
from tkinter import Button
from tkinter import END
from tkinter import Entry

class CalculatorGUI:

    def __init__(self, master, controller):

        self.master = master
        self.master.title('Ethernity')
        self.master.geometry()
        self.controller = controller
        self.entry = Entry(master)
        self.entry.grid(row=0, column=0, columnspan=6)
        self.entry.focus_set()

        #UI desing
        Button(self.master, text="7", width=3, command=lambda: self.inputVal(7)).grid(row=1, column=0)
        Button(self.master, text="4", width=3, command=lambda: self.inputVal(4)).grid(row=2, column=0)
        Button(self.master, text="1", width=3, command=lambda: self.inputVal(1)).grid(row=3, column=0)
        Button(self.master, text="8", width=3, command=lambda: self.inputVal(8)).grid(row=1, column=1)
        Button(self.master, text="5", width=3, command=lambda: self.inputVal(5)).grid(row=2, column=1)
        Button(self.master, text="2", width=3, command=lambda: self.inputVal(2)).grid(row=3, column=1)
        Button(self.master, text="0", width=3, command=lambda: self.inputVal(0)).grid(row=4, column=1)
        Button(self.master, text="9", width=3, command=lambda: self.inputVal(9)).grid(row=1, column=2)
        Button(self.master, text="6", width=3, command=lambda: self.inputVal(6)).grid(row=2, column=2)
        Button(self.master, text="3", width=3, command=lambda: self.inputVal(3)).grid(row=3, column=2)

        # Behavior Functions
        Button(self.master, text='AC', width=3, command=lambda: self.clearAll()).grid(row=1, column=4)
        Button(self.master, text='C',  width=3, command=lambda: self.deleteOne()).grid(row=2, column=4)

        # MAth Functions
        Button(master, text="sin",   width=3, command=lambda: self.controller.buttonevent(btn.sin)).grid(row=1, column=5)
        Button(master, text="e^(x)", width=3, command=lambda: self.controller.buttonevent(btn.epowx)).grid(row=2, column=5)
        Button(master, text="10^x",  width=3, command=lambda: self.controller.buttonevent(btn.tenPowx)).grid(row=3, column=5)
        Button(master, text="√",     width=3, command=lambda: self.controller.buttonevent(btn.sqr)).grid(row=3, column=4)
        Button(master, text="ln(x)", width=3, command=lambda: self.controller.buttonevent(btn.loge)).grid(row=4, column=4)

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