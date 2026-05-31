class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        res = nums[l]
        while l <= r:
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                return res
            middle = (l + r) // 2
            res = min(res, nums[middle])
            if nums[middle] >= nums[l]:
                l = middle + 1
            else:
                r = middle - 1
            print(middle)
        return res