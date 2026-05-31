class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        postfix = []
        x,y = 1, 1

        for i in range(len(nums)):
            # for prefix
            prefix.append(x)
            x *= nums[i]

            # for postfix
            postfix.append(y)
            y*= nums[-i-1]
        
        total = []
        for i in range(len(prefix)):
            total.append(prefix[i] * postfix[-i-1])

        return total