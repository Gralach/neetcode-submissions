class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprofit = 0
        i = 0
        j = i+1
        while j <= len(prices)-1:
            if prices[j] < prices[i]:
                print("check")
                i = j
                j = i+1
            else:
                maxprofit = max(maxprofit, prices[j] - prices[i])
                j += 1
        return maxprofit
                