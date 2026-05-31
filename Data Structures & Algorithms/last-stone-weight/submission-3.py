class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        self.stones = stones
        heapq.heapify_max(stones)
        while(len(stones)) > 1:
            x = heapq.heappop_max(stones)
            y = heapq.heappop_max(stones)
            if x == y:
                if not stones:
                    return 0
            else:
                heapq.heappush_max(stones, abs(x - y))
        return heapq.heappop_max(stones)