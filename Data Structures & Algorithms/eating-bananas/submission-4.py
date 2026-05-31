class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        minim, maxim = 1, max(piles)
        res = maxim
        while minim <= maxim:
            middle = (minim + maxim) // 2
            temp = 0
            for i in piles:
                temp += math.ceil(i / middle)
            if temp <= h:
                maxim = middle - 1
                res = middle
            else:
                minim = middle + 1
        return res