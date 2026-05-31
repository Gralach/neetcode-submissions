class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for i, x in enumerate(nums):
            if x in nums[i+1:]:
                return True
            else:
                continue
        return False