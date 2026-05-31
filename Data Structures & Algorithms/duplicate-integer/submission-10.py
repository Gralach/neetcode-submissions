class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        check = defaultdict()
        for i in nums:
            if i in check:
                return True
            check[i] = True
        return False
        