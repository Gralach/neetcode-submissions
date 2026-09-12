class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        check = [0] *3
        for i in nums:
            check[i] += 1
        x, bucket = 0, 0
        while x < len(nums):
            for j in range(0, check[bucket]):
                nums[x] = bucket
                x += 1
            bucket += 1    