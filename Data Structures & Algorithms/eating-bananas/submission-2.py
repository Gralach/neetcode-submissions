class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        maxpile = max(piles)
        l = 1
        r = maxpile
        res = r

        while l <=r:
            k = (l + r) //2
            time = 0
            for x in piles:
                time += math.ceil(x / k)
            if h >= time:
                r = k - 1
                res = min(res, k)
            else:
                l = k + 1
        return res