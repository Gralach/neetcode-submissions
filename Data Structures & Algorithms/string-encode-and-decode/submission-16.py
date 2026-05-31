class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for i in strs:
            res += f"{len(i)}#{i}"
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        start = 0
        curindex = 0
        while curindex < len(s):
            if s[curindex] == "#":
                length = int(s[start:curindex]) + 1
                start = curindex + length
                res.append(s[curindex + 1: curindex + length])
                curindex = start
            curindex += 1
        return res