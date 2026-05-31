class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1]
        postfix = [1]

        for i, v in enumerate(nums):
            prefix.append(prefix[i]*v)
            postfix.append(postfix[i]*nums[-(i+1)])
        print(prefix, postfix)
        res = []
        for i in range(len(prefix) - 1):
            res.append(prefix[i] * postfix[-(i+2)])
        return(res)