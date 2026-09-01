import math

class AreaCalc:
    def calculate(self, x, y = None):
        if y is None:
            return round(math.pi * x**2, 2)
        else:
            return x * y
    

    
# Don't modify the following code
calc = AreaCalc()
print(calc.calculate(5))    
print(calc.calculate(4, 6))
