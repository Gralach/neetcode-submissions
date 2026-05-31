class Solution:

    def encode(self, strs: List[str]) -> str:
        text = ""
        for string in strs:
            text += f"{len(string)}#{string}"
        return text

    def decode(self, s: str) -> List[str]:
        res = []
        i , j = 0, 0
        while j < len(s):
            if s[j] == "#":
                res.append(s[j+1:j+int(s[i:j])+1])
                i = j = j+int(s[i:j])+1
            j += 1
        return(res)