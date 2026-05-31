class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        i = 1
        j = max(piles)
        mink = 1
        
        while i <= j:
            k = (i+j)//2
            print(k)
            temp = 0
            for x in piles:
                temp += math.ceil(x/k)
            if temp <= h:
                j = k - 1
                mink = k
            else:
                i = k + 1
        return mink
        