class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        prev = prices[0]
        profit = 0
        for i in range(1, len(prices)):
            print(prices[i])
            profit = max(profit, prices[i]- prev)
            prev = min(prices[i], prev)
        return profit