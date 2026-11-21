class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        minPrice = 10000000
        maxProfit = 0

        for price in prices:
            minPrice = min(price, minPrice)

            profit = price - minPrice
            maxProfit = max(maxProfit, profit)
        
        return maxProfit

        