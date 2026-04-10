class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0 
        current_min = float('inf')
        for price in prices:

            current_min = min(current_min, price)
            profit = price - current_min
            max_profit = max(max_profit, profit)
        
        return max_profit
