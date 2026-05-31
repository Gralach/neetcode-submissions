class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for i in strs:
            encoded += str(len(i)) + "#" + i
        return encoded

    def decode(self, s: str) -> List[str]:
        decoded, i = [], 0

        while i < len(s):
            j = i
            while s[i] != "#":
                i += 1
            length = int(s[j:i])
            decoded.append(s[i+1:i+1+length])
            i += length +1
        return decoded
