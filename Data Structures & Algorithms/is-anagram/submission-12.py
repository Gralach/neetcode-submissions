class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        check_s = defaultdict(int)
        check_t = defaultdict(int)
        
        for i in range(len(s)):
            check_s[s[i]] += 1
            check_t[t[i]] += 1
        if check_s == check_t:
            return True
        return False