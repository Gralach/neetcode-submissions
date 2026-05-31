class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        checks, checkt = defaultdict(int), defaultdict(int)

        if len(s)!= len(t):
            return False
        for i in range(len(s)):
            checks[s[i]] += 1
            checkt[t[i]] += 1
        
        if checks == checkt:
            return True
        return False
            
