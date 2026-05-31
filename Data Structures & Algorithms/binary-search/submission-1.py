class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def check(l, r, lists):
            index = l + (r-l)//2
            if (l > r):
                return -1
            elif (lists[index] == target):
                return index
            elif lists[index] > target:
                return check(l, index-1, lists)
            else:
                return check(index+1, r, lists)
        l = 0
        r = len(nums) - 1
        return check(l, r, nums)