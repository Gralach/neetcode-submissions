class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        check1 = defaultdict(int)
        check2 = defaultdict(int)
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            check1[s[i]] += 1
            check2[t[i]] += 1

        print(check1)
        print(check2)
        if check1 == check2:
            return True
        else:
            return False

        