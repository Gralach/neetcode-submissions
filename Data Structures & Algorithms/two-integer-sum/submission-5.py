class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        check = defaultdict(int)

        for i,v in enumerate(nums):
            if v in check:
                return [check[v], i]
            check[target-v] = i
            