class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i, x in enumerate(nums):
            if x not in dic:
                dic[target - x] = i
            else:
                return [dic[x], i]  