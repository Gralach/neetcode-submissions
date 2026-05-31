class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        saved = defaultdict(int)
        for i in nums:
            saved[i] += 1
        top_k = []
        for x in range(k):
            top = max(zip(saved.values(), saved.keys()))[1]
            top_k.append(top)
            saved.pop(top)
        return top_k