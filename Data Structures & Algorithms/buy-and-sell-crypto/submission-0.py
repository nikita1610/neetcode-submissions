class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_start = float('inf')
        for price in prices :
            min_start = min(min_start, price)
            max_profit = max(max_profit, price-min_start)
        return max_profit