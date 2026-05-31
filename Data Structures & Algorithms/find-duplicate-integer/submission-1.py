class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        check = defaultdict(bool)
        for i in nums:
            if i in check:
                return i
            check[i] = True