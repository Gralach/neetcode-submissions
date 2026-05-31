class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        check = defaultdict(int)
        for i in range(len(nums)):
            if nums[i] in check:
                return [check[nums[i]], i]
            remainder = target - nums[i]
            check[remainder] = i