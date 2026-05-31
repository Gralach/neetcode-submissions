class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        check = set()
        maxlength = 0
        l = 0
        for i in range(len(s)):
            while s[i] in check:
                check.remove(s[l])
                l+=1
            check.add(s[i])
            maxlength = max(len(check), maxlength)
        return maxlength