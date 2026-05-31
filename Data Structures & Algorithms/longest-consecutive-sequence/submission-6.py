class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        check = set(nums)
        curmax = 0
        for i, v in enumerate(nums):
            if v-1 not in check:
                length = 0
                while v + length in check:
                    length += 1
                curmax = max(curmax, length)
        return curmax