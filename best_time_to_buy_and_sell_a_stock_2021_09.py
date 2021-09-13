'''
7 1 5 3 6 4
  i     j
'''
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprofit = 0
        runningprofit = float("-inf")
        i = 0
        for j in range(len(prices)):
            if prices[j] < prices[i]:
                i = j
            runningprofit = prices[j] - prices[i]
            maxprofit = max(maxprofit, runningprofit)
        return maxprofit