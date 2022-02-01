class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = max(prices) + 1
        maxProfit = 0
        for index, price in enumerate(prices):
            minPrice = min(minPrice, price)
            if price > minPrice:
                maxProfit = max(maxProfit, price-minPrice)
        return maxProfit