class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy =prices[0]
        prof=0

        for i in range(1,len(prices)):
            if prices[i] < buy:
                buy=prices[i]
            elif prices[i] - buy > prof:
                prof = prices[i] - buy
        return prof
        