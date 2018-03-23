__author__ = "The CalculatorPro Inc."
__copyright__ = "Copyright 2018, CalculatorPro"
__credits__ = ["Team A"]
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "Beranrdo Sandi"
__email__ = "B_SANDI@encs.concordia.ca"
__status__ = "Release v1.0"


from tkinter import *
from Controller import *

#Initialize calculator

def __init__(self, master):
    master.title('ETERNITY')
    master.geometry()
    self.e = Entry(master, font = ("Times", 15, 'bold'))
    self.e.grid(row=0, column=0, columnspan=10, sticky = W+E)
    self.e.focus_set()




        # Creating Buttons

        # Number Pad
    Button(master, text="7", width=3, command=lambda: self.inputVal(7), font=("times", 15)).grid(row=1, column=0)
    Button(master, text="4", width=3, command=lambda: self.inputVal(4), font=("times", 15)).grid(row=2, column=0)
    Button(master, text="1", width=3, command=lambda: self.inputVal(1), font=("times", 15)).grid(row=3, column=0)
    Button(master, text="0", width=3, command=lambda: self.inputVal(0), font=("times", 15)).grid(row=4, column=0)

    Button(master, text="8", width=3, command=lambda: self.inputVal(8), font=("times", 15)).grid(row=1, column=1)
    Button(master, text="5", width=3, command=lambda: self.inputVal(5), font=("times", 15)).grid(row=2, column=1)
    Button(master, text="2", width=3, command=lambda: self.inputVal(2), font=("times", 15)).grid(row=3, column=1)
    Button(master, text=".", width=3, command=lambda: self.inputOperator('.'), font=("times", 15)).grid(row=4, column=1)

    Button(master, text="9", width=3, command=lambda: self.inputVal(9), font=("times", 15)).grid(row=1, column=2)
    Button(master, text="6", width=3, command=lambda: self.inputVal(6), font=("times", 15)).grid(row=2, column=2)
    Button(master, text="3", width=3, command=lambda: self.inputVal(3), font=("times", 15)).grid(row=3, column=2)
    Button(master, text="=", width=3, command=lambda: self.calculate('='), font=("times", 15), foreground = "red").grid(row=4, column=2)


        # Functions
    Button(master, text='C', width=3, command=lambda: self.deleteOne(), font=("times", 15), foreground="red").grid(row=1, column=4)
    Button(master, text="*", width=3, command=lambda: self.inputOperator('*'), font=("times", 15)).grid(row=2, column=4)
    Button(master, text="+", width=3, command=lambda: self.inputOperator('+'), font=("times", 15)).grid(row=3,column=4)
    Button(master, text="(", width=3, command=lambda: self.inputOperator('('), font=("times", 15)).grid(row=4,column=4)

    Button(master, text='AC', width=3, command=lambda: self.clearAll(), font=("times", 15),foreground="red").grid(row=1, column=5)
    Button(master, text="/", width=3, command=lambda: self.inputOperator('/'), font=("times", 15)).grid(row=2,column=5)
    Button(master, text="-", width=3, command=lambda: self.inputOperator('-'), font=("times", 15)).grid(row=3,column=5)
    Button(master, text=")", width=3, command=lambda: self.inputOperator(')'), font=("times", 15)).grid(row=4,column=5)

    Button(master, text="√", width=3, command=lambda: self.squareroot(), font=("times", 15)).grid(row=1, column=6)
    Button(master, text="ln(x)", width=3, command=lambda: self.ln(), font=("times", 15)).grid(row=2, column=6)
    Button(master, text="sin", width=3, command=lambda: self.sine(), font=("times", 15)).grid(row=3, column=6)
    Button(master, text="e^(x)", width=3, command=lambda: self.exFunc(), font=("times", 15)).grid(row=4, column=6)

    Button(master, text="10^x", width=3, command=lambda: self.tenToPower(), font=("times", 15)).grid(row=1, column=7)




# def main():
#     pass
#     root = Tk()
#     object = calculator(root)  # object instantiated
#     root.mainloop()
#
#
#
# if __name__ == "__main__":
#     main()
# else:
#     pass



# Main
cal = Tk()
#object = calculator(root)  # object instantiated
cal.mainloop()