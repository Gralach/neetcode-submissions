class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        check = defaultdict(int)
        for index, i in enumerate(nums):
            if target - i in check.keys():
                return [check[target-i], index]
            check[i] = index