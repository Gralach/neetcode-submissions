class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack , result = [], []
        def backtrack(openC, closedC):
            if openC == closedC == n :
                result.append("".join(stack))
                return
            if openC < n:
                stack.append("(")
                backtrack(openC+1, closedC)
                stack.pop()
            if closedC < openC:
                stack.append(")")
                backtrack(openC, closedC+1)
                stack.pop()
        backtrack(0,0)
        return result
            
        