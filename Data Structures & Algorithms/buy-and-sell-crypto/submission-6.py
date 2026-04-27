class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        max_profit = 0
        buy_price = float('inf')
        
        for price in prices:
            if price < buy_price:
                buy_price = price
            
            tmp_profit = price - buy_price

            max_profit = max(max_profit,tmp_profit)
        
        return max_profit