class Solution:
    def sort(self, nums):
        if len(nums) <= 1:
            return nums
        first_part = []
        second_part = []
        pivot = nums[len(nums)//2]
        for i in range(len(nums)):
            if i == len(nums)//2:
                continue
            else:
                if nums[i] > pivot:
                    second_part.append(nums[i])
                else:
                    first_part.append(nums[i])
        return self.sort(first_part) + [pivot] + self.sort(second_part)

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = self.sort(nums)
        final = []
        for i in range(len(nums)):
            j = i+1
            k = len(nums)-1
            while j < k:
                if [nums[i], nums[j], nums[k]] in final:
                    k-=1
                elif nums[i] + nums[j] + nums[k] > 0:
                    k-= 1
                elif nums[i] + nums[j] + nums[k] < 0:
                    j+=1
                else:
                    final.append([nums[i], nums[j], nums[k]])
                    k-=1
        return final
