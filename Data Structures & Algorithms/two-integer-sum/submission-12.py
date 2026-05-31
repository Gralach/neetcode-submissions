class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = defaultdict(int)
        for i, v in enumerate(nums):
            if target - v in res:
                return [res[target-v], i]
            res[v] = i
            print(res)