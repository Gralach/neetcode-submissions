class Solution:
    def isValid(self, s: str) -> bool:
        check = []
        if (len(s) == 1) or (s[0] not in ["{", "(" , "["]):
            return False
        for i in s:
            if i in ["{", "(" , "["]:
                check.append(i)
            elif (check and ((i == "}" and check[-1] == "{") or 
                (i == ")" and check[-1] == "(") or
                (i == "]" and check[-1] == "["))):
                check.pop()
            else:
                return False
        if not check:
            return True
        else:
            return False