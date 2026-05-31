class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        checks = defaultdict(int)
        checkt = defaultdict(int)
        for i, v in enumerate(s):
            checks[v] +=1
            checkt[t[i]] +=1
        if checks == checkt:
            return True
        return False