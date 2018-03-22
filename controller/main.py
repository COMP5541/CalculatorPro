from tkinter import Tk
from tkinter import END
from view.main import CalculatorGUI as View
import model.sin as sin
import model.funEx as funEx
import model.ln as ln
import model.squareroot as squareroot
import model.tentopowerx as tentopowerx
from commonAssets.main import Button as btn
import decimal

class Controller():

    def __init__(self):
        self.root = Tk()
        self.view = View(self.root, self)
        #self. model = Model

    def run(self):
        self.root.mainloop()

    def buttonevent(self,function):

        d = decimal.Decimal

        entry = self.getEntry()
        result = 0

        if (self.isWithinRange(entry)):
            if (function==btn.loge):
                result = ln.loge(entry)
            elif (function==btn.sqr):
                result = squareroot.squareroot(entry)
            elif (function==btn.tenPowx):
                result = tentopowerx.tentopower(entry)
            elif (function==btn.sin):
                result = sin.sin(entry)
            elif (function==btn.ePowx):
                result = 1
            else:
                pass
            self.clearEntry()
            self.writeEntry(self.formatOutput(result))
        else:
            result = 'Out of Range'
            self.clearEntry()
            self.writeEntry(result)


    def getEntry(self):
        return eval(self.view.entry.get())

    def clearEntry(self):
        self.view.entry.delete(0, END)

    def writeEntry(self,result):
        self.view.entry.insert(0, result)

    def isWithinRange(self,num):
        result = True
        if (num > 10000000000 or num < -10000000000):
            result = False
        return result

    def formatOutput(self,num):
        numStr = "{0:.7f}".format(num)
        if (numStr == '-0.0000000'):
            return '0'
        elif (numStr == '0.0000000'):
            return '0'
        elif (numStr == '-1.0000000'):
            return '1'
        elif (numStr == '1.0000000'):
            return '1'
        else:
            return numStr

if __name__ == '__main__':
    Controller().run()