class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_i, temp = 0, 0
        for i in nums:
            if i == 1:
                temp += 1
            else:
                max_i = max(max_i, temp)
                temp = 0
        return max(max_i,temp)