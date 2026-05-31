class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        i = 0
        res = []
        for i in range(len(nums)):
            j, k = i + 1, len(nums)-1
            while j < k:
                if (nums[i]+nums[j]+nums[k] == 0):
                    if [nums[i], nums[j], nums[k]] in res:
                        k -= 1
                    else:
                        res.append([nums[i],nums[j],nums[k]])
                        k -= 1
                elif (nums[i] + nums[j] + nums[k] > 0):
                    k -=1
                else:
                    j += 1
        return res

        