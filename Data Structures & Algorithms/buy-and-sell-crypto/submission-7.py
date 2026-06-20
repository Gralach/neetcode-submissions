class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = []
        maxprofit = 0
        for i in range(len(prices)):
            res.append(prices[i])
            if prices[i] < res[0]:
                res = [prices[i]]
            print(res)
            maxprofit = max(maxprofit, prices[i] - res[0])
        return(maxprofit)