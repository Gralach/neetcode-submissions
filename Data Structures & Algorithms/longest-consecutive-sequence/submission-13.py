class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums = list(sorted(set(nums)))
        print(nums)
        res, count = 1, 1
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1] + 1:
                count += 1
            else:
                res = max(count, res)
                count = 1
        return max(res,count)