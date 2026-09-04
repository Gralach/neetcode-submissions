class Solution:
    def isValid(self, s: str) -> bool:
        # opening = "[{("
        closing = ")}]"
        check = []
        for i in s:
            print(check)
            if (i in closing) and check:
                if i == "}" and check[-1] == "{":
                    check.pop()
                elif i == ")" and check[-1] == "(":
                    check.pop()
                elif i == "]" and check[-1] == "[":
                    check.pop()
                else:
                    return False
            else:
                check.append(i)
        if check:
            return False
        return True
            