class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        chars = {}
        chart = {}
        s_length = len(s)
        if s_length != len(t):
            return False
        for i in range(s_length):
            if s[i] not in chars:
                chars[s[i]] = 1
            elif s[i] in chars:
                chars[s[i]] += 1
            
            if t[i] not in chart:
                chart[t[i]] = 1
            elif t[i] in chart:
                chart[t[i]] += 1

        if chars == chart:
            return True
        else:
            return False
        