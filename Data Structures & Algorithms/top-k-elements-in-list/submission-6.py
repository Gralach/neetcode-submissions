class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        check = defaultdict(int)
        for i in nums:
            check[i] += 1
        res = []
        for i in range(k):
            top = max(zip(check.values(), check.keys()))[1]
            res.append(top)
            check.pop(top)
        return res