import decimal
from model.baseFunction import CommonToFunction as CTF
from model.sin import Sin

class CalculatorFunction(CTF):

    def __init__(self):
        self.d = decimal.Decimal
        #init sin with default parameter
        self.sin = Sin()

    def Sin(self,num):
        a = self.sin.calculate(num)
        return self.formatOutput(a)

    def formatOutput(self,num):
        return super().formatOutput(num)

def main():
    d = decimal.Decimal
    #test sin
    print(CalculatorFunction().Sin(3.14))
    #test pi
    print(CalculatorFunction().formatOutput(CalculatorFunction().piconstant()))

if __name__ == '__main__':
    main()