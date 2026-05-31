class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "~" + s
        print(res)
        return res

    def decode(self, s: str) -> List[str]:
        start, curr = 0, 0
        res = []
        while curr < len(s):
            if s[curr] == "~":
                length = int(s[start:curr])
                start = curr+1+length
                res.append(s[curr+1:start])
            curr +=1
        return res