class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        check = {}
        for i in range(len(nums)):
            if nums[i] not in check.keys():
                check[target - nums[i]] = i
            else:
                return([check[nums[i]], i])
        