class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxlen = 0
        temp = []
        for i in s:
            if ord(i) not in temp:
                temp.append(ord(i))
            else:
                temp = temp[temp.index(ord(i))+1:]
                temp.append(ord(i))
            maxlen = max(len(temp), maxlen)
        return maxlen