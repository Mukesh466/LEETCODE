class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        buy=prices[0]
        profit=0
        for i in range(0,len(prices)):
            if prices[i] > buy:
                profit += prices[i]-buy
            buy=prices[i]
        return profit