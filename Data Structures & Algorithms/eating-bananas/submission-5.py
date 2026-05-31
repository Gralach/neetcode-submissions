class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        minim = 1
        maxim = max(piles)
        res = maxim

        while minim <= maxim:
            rate = (minim + maxim) // 2
            print(rate)
            temp = 0
            for i in piles:
                temp += math.ceil(i / rate)
            if temp > h:
                minim = rate + 1
            else:
                maxim = rate - 1
                res = min(rate, res)
        return res