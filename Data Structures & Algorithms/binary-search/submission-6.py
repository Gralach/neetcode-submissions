class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) -1 
        while l <= r:
            middle = (l + r) // 2
            print(middle)
            if nums[middle] == target:
                return middle
            elif nums[middle] < target:
                l = l + 1
            else:
                r = r - 1
        return -1