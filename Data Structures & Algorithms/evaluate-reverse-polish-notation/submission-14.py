class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i not in "+-/*":
                stack.append(i)
            else:
                if len(stack) > 1:
                    a, b = stack.pop(), stack.pop()
                    stack.append(int(eval(f"{b}{i}{a}")))
                else:
                    return int(stack.pop())
                    
        return int(stack.pop())