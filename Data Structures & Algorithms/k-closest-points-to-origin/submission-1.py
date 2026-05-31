class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dist = []
        for i in points:
            x, y = i
            dist.append([x**2 + y**2, x, y])
        heapq.heapify(dist)
        res = []
        while k > 0:
            _, x, y = heapq.heappop(dist)
            res.append([x, y])
            k-= 1
        return res