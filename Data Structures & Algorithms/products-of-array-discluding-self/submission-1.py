class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        x, y = 1, 1
        prefix = []
        postfix = []
        postfix.append(x)
        prefix.append(y)
        for i in range(len(nums)):
            x = nums[i] * x
            prefix.append(x)
            y = nums[len(nums)-1-i] * y
            postfix.append(y)
        final = []
        for j in range(len(prefix[:-1])):
            final.append(prefix[j] *postfix[len(prefix) - 2 - j])
        return final