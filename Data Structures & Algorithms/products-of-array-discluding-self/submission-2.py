class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        postfix = []
        prefix.append(1)
        postfix.append(1)

        for i, v in enumerate(nums):
            prefix.append(prefix[i]*v)
            postfix.append(postfix[i]*nums[len(nums)-1-i])
        final = []
        for i in range(len(postfix) - 1):
            final.append(postfix[len(postfix) - 2 - i] * prefix[i])
        return(final)
        