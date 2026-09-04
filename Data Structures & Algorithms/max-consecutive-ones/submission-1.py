class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res, temp = 0, 0
        for i in nums:
            if i == 1:
                temp += 1
            else:
                res = max(res, temp)
                temp = 0
        return max(res, temp)