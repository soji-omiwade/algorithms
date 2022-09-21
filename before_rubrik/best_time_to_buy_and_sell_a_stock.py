from typing import List 
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = 0
        max_profit = 0
        for j in range(len(prices)):
            if prices[j] < prices[i]:
                i = j
            max_profit = max(max_profit, prices[j] - prices[i])
        return max_profit
        
    def maxProfitDP(self, prices: List[int]) -> int:
        max_profit = max_curr = 0
        for i in range(1, len(prices)):
            max_curr += prices[i] - prices[i-1]
            max_curr = max(0, max_curr)
            max_profit = max(max_curr, max_profit)
        return max_profit