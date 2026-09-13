class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def eat(rate, piles):
            total = 0
            for banana in piles:
                total += math.ceil(banana / rate)
            return total

        low, high = 1, max(piles)
        ans  = high
        while low <= high:
            middle = (low + high) // 2
            if eat(middle, piles) > h:
                low = middle + 1
            else:
                high = middle - 1
                ans = min(ans, middle)
        return ans