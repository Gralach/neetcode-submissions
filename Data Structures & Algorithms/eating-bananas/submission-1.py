class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        k = max(piles)
        minj=1
        i = 1
        while i <= k:
            j = (i+k)//2
            temp = 0
            for x in piles:
                temp+= math.ceil(x/j)
            print(temp)
            print(h)
            if temp > h:
                i = j + 1
            else:
                k = j - 1
                minj = j
        return minj 
