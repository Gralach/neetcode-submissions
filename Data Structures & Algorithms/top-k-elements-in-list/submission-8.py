class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        check = defaultdict(int)
        for index, i in enumerate(nums):
            check[i] += 1
        res = []
        for i in range(k):
            temp = max(zip(check.values(),check.keys()))
            res.append(temp[1])
            check.pop(temp[1])
        return res