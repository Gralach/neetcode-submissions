class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        elements = {}
        for i in nums:
            if i not in elements:
                elements[i] = 1
            else:
                elements[i] += 1
        kFreq = []
        for i in range(k):
            most = max(zip(elements.values(), elements.keys()))[1]
            kFreq.append(most)
            elements.pop(most)
        return kFreq