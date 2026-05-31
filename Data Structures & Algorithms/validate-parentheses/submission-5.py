class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2 !=0:
            return False
        else:   
            stack = []
            lbrackets = {")":"(", 
                        "}":"{", 
                        "]":"["}
            for i in s:
                if ((i in lbrackets.keys()) and (len(stack) > 0)):
                    if stack[-1] == lbrackets[i]:
                        stack.pop()
                    else:
                        return False
                else:
                    stack.append(i)
            if len(stack) == 0:
                return True
            else:
                return False