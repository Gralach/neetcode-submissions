class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        if len(tokens) == 1:
            return int(tokens.pop())
        for i in range(len(tokens)):
            if tokens[i].strip("-").isnumeric():
                stack.append(tokens[i])
            else:
                a = stack.pop()
                b = stack.pop()
                total = int(eval(f"{b}{tokens[i]}{a}"))
                stack.append(total)
        return stack.pop()