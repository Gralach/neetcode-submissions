class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        saved = defaultdict(int)
        for i in nums:
            saved[i] += 1
        top_k = []
        for i in range(k):
            item = max(zip(saved.values(), saved.keys()))[1]
            top_k.append(item)
            saved.pop(item)
        return top_k 