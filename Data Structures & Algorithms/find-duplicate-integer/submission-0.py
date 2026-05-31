class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        check = defaultdict(int)
        for i in nums:
            if i in check.keys():
                return i
            check[i] == True