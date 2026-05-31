class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        check = defaultdict(int)
        for i in nums:
            if check[i]:
                return True
            check[i] = True
        return False