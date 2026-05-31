class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        check = defaultdict(int)
        for i in nums:
            check[i] += 1
        res = []
        while k:
            temp = list(max(zip(check.values(), check.keys())))[1]
            res.append(temp)
            check.pop(temp)
            k-=1
        return res