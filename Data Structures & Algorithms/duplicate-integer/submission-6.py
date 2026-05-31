class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dic = defaultdict(int)
        for i in nums:
            if i not in dic:
                dic[i] = True
            else:
                return True
        return False