class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prev = [1]
        post = [1]
        for i in range(len(nums)):
            prev.append(prev[i]*nums[i])
            post.append(post[i]*nums[len(nums)-i-1])
        res = []
        prev, post = prev[:-1], post[:-1][::-1] 
        for i in range(len(prev)):
            res.append(prev[i] * post[i])
        return(res)