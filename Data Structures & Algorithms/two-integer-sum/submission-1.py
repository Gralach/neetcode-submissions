class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sums = {}
        for i in range(len(nums)):
            check = target - nums[i]
            if check in sums.keys():
                return [sums[check], i]
            sums[nums[i]] = i
