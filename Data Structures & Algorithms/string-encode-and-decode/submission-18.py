class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""
        res = ""
        for i in strs:
            res += f"{len(i)}#{i}"
        return res

    def decode(self, s: str) -> List[str]:
        if not s:
            return []
        last_i, i = 0, 0
        res = []
        while i <= len(s):
            if s[i] == "#":
                last_i = i+1+int(s[last_i:i])
                print(last_i)
                res.append(s[i+1 : last_i])
                i = last_i
            i += 1
        return res