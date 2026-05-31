class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        res = defaultdict(bool)
        for x in nums:
            if x in res:
                return True
            res[x] = True
        return False