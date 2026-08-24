class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        check = defaultdict(int)
        for i in nums:
            check[i] += 1
            if check[i] > len(nums) / 2:
                return i
        