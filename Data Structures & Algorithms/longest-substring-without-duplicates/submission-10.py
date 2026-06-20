class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        temp = []
        res = 0
        for i in s:
            while i in temp:
                temp.pop(0)
            temp.append(i)
            res = max(res, len(temp))
        return res