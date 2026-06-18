class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        i, j, k = 0, 1, len(nums)-1
        nums = sorted(nums)
        res = []

        while  i < j < k:
            while j < k:
                if (nums[i] + nums[j] + nums[k]) == 0:
                    if [nums[i],nums[j],nums[k]] not in res:
                        res.append([nums[i],nums[j],nums[k]])
                    j += 1
                elif (nums[i] + nums[j] + nums[k]) > 0:
                    k -= 1
                else:
                    j += 1
            i+=1
            j,k = i+1, len(nums)-1
        return res           

        