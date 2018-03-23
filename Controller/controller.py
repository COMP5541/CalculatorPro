__author__ = "The CalculatorPro Inc."
__copyright__ = "Copyright 2018, CalculatorPro"
__credits__ = ["Team A"]
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "Beranrdo Sandi"
__email__ = "B_SANDI@encs.concordia.ca"
__status__ = "Release v1.0"

from tkinter import *
#import parser
from Model import funEx, ln, sin, squareroot, tentopowerx




class calculator:
   def clearAll(self):
       self.e.delete(0, END)

   def deleteOne(self):
       self.txt = self.e.get()[:-1]
       self.e.delete(0, END)
       self.e.insert(0, self.txt)

   def inputVal(self, argi):
       self.e.insert(END, argi)

   def inputOperator(self, operator):
       self.e.insert(END, operator)

   def calculate(self):
       self.value= eval(self.e.get())
       try:
          formula = self.e.get()#parser.expr(self.value).compile()
          result = eval(formula)
          self.clearAll()
          self.e.insert(0, result)
       except Exception:
          self.clearAll()
          self.e.insert(0, "Error!")


    # Functions

# Squareroot function
   def squareroot(self):
     self.value = eval(self.e.get())
     self.sqrtval = squareroot.squareroot(self.value)
     self.e.delete(0, END)
     self.e.insert(0, self.sqrtval)


    # Natural Logarithm function
   def ln(self):
     self.value = eval(self.e.get())
     self.sqrtval = ln.loge(self.value)
     self.e.delete(0, END)
     self.e.insert(0, self.sqrtval)

    # Ten to the power function
   def tenToPower(self):
     self.value = eval(self.e.get())
     self.sqrtval = tentopowerx.tentopower(self.value)
     self.e.delete(0, END)
     self.e.insert(0, self.sqrtval)


    # e to the power function
   def exFunc(self):
     self.value = eval(self.e.get())
     self.sqrtval = funEx.fun_ex(self.value)
     self.e.delete(0, END)
     self.e.insert(0, self.sqrtval)

    # Sine  function
   def sine(self):
     self.value = eval(self.e.get())
     self.sqrtval = sin.sin(self.value)
     self.e.delete(0, END)
     self.e.insert(0, self.sqrtval)


