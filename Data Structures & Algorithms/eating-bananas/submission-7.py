class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def eat(rate, piles):
            total = 0
            print("start")
            for banana in piles:
                print(math.ceil(banana / rate))
                total += math.ceil(banana / rate)
            print("total", total)
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