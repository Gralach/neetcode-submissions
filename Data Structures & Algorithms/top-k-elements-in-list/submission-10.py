class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = defaultdict(int)
        for i in nums:
            res[i] += 1
        final = []    
        for i in range(k):
            num = max(zip(res.values(),res.keys()))
            res.pop(num[1])
            final.append(num[1])
        return final