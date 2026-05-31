class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        check = set(nums)
        maxnum = 0
        for i in nums:
            if i - 1 not in check:
                length = 0
                while i+length in check:
                    length += 1
                maxnum = max(maxnum, length)
        return maxnum
        