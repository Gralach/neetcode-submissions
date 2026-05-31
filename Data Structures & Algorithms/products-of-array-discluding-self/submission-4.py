class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix, postfix = [1], [1]

        for i, _ in enumerate(nums):
            prefix.append(nums[i] * prefix[i])
            postfix.append(nums[len(nums)-i-1] * postfix[i])
        res = []
        for i in range(len(prefix)-1):
            res.append(prefix[i] * postfix[len(prefix)-2-i])
        return res