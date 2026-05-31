class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        s_ele = defaultdict(int)
        t_ele = defaultdict(int)

        for i in range(len(s)):
            s_ele[s[i]] += 1
            t_ele[t[i]] += 1

        if s_ele == t_ele:
            return True
        return False