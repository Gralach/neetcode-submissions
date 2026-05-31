class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        nums = set(nums)
        if len(nums) == 1:
            return 1
            
        for i in nums:
            if i-1 in nums:
                temp = 0
                cur = i
                while True:
                    if cur in nums:
                        temp += 1
                        cur -= 1
                    else:
                        break
                res = max(res, temp)
        return res