class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sums = defaultdict(int)
        for i in range(len(nums)):
            if nums[i] in sums:
                return [sums[nums[i]], i]
            sums[target - nums[i]] = i