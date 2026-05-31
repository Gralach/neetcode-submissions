class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        res = nums[l]
        while l <= r:
            if nums[l] < nums[r]:
                res = min(nums[l], res)
                break
            k = (l+r)//2
            res = min(res, nums[k])
            if nums[k] >= nums[l]:
                l = k + 1
            else:
                r = k - 1
        return(res)
        