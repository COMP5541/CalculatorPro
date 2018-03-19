import decimal
from model.bFunction import CommonToFunction as CTF

class CalcFunction(CTF):

    # TODO -- use own power function implmentation
    def arctan(self,x):
        d = decimal.Decimal
        with decimal.localcontext() as context:
            context.prec += 4
            result = d(0)
            for n in range(0, 20, 1):
                result = result + ((d(-1)) ** n) * (x ** (d(2) * n + d(1))) / (d(2) * n + d(1))
        return result

    def piconstant(self):
        d = decimal.Decimal
        return d(4) * (d(4) * self.arctan((d(1 / 5)) - self.arctan(d(1 / 239))))

    def formatOutput(self,num):
        super().formatOutput()

def main():
    testPi = CalcFunction()
    print(testPi.piconstant())

if __name__ == '__main__':
    main()