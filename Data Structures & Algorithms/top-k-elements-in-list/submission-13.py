class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        temp = defaultdict(int)
        for i, v in enumerate(nums):
            temp[v] += 1
        res = []
        for i in range(k):
            cur = max(zip(temp.values(), temp.keys()))[1]
            temp.pop(cur)
            res.append(cur)
        return(res)