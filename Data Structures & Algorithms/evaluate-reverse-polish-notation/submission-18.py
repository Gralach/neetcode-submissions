class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        calc = []
        for i in tokens:
            calc.append(i)
            if i in ["+", "-", "*", "/"]:
                print("calculating")
                print(calc)
                operation, num2, num1 = calc.pop(), int(calc.pop()), int(calc.pop())
                if operation == "+":
                    calc.append(num1+num2)
                elif operation == "-":
                    calc.append(num1-num2)
                elif operation == "*":
                    calc.append(num1*num2)
                elif operation == "/":
                    calc.append(int(num1/num2))
        return int(calc[0])