class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        res = 0

        for i in nums:
            temp, count = i, 0
            while temp in nums:
                temp -=1
                count += 1
            res = max(res, count)
        return res