class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        minim = 1
        maxim = max(piles)
        res = maxim

        while minim <= maxim:
            rate = (maxim + minim) //2
            temp = 0
            for i in piles:
                temp += math.ceil(i/rate)
            if temp <= h:
                maxim = rate - 1
                res = rate
            else:
                minim = rate + 1
        return res
