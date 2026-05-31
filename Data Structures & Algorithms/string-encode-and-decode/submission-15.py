class Solution:

    def encode(self, strs: List[str]) -> str:
        combined = ""
        for i in strs:
            combined += f"{len(i)}#{i}"
        return combined

    def decode(self, s: str) -> List[str]:
        cur, temp = 0, 0
        decoded = []
        while cur < len(s):
            if s[temp] != "#":
                temp += 1
            else:
                length = int(s[cur:temp])
                text = s[temp+1: temp+ length + 1]
                decoded.append(text)
                cur = temp + length + 1
                temp = cur
        return decoded
