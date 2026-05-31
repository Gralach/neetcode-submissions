class Solution:

    def encode(self, strs: List[str]) -> str:
        string = ""
        for i in strs:
            string += f"{len(i)}#{i}"
        return string

    def decode(self, s: str) -> List[str]:
        text = []
        i, j = 0, 0
        while i < len(s):
            if s[j] != "#":
                j += 1
            else:
                num = int(s[i:j])
                i = j+1+num
                text.append(s[j+1:i])
                j = i
        return text