class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        checks = defaultdict(int)

        for i, v in enumerate(nums):
            if target - v in checks.keys():
                return [checks[target - v], i]
            checks[v] = i
