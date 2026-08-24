class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        checkS, checkT = defaultdict(int), defaultdict(int)

        if len(s) != len(t):
            return False

        for i in range(len(s)):
            checkS[s[i]] += 1
            checkT[t[i]] += 1

        if checkS == checkT:
            return True
        
        return False