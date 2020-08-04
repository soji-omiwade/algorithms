from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprofit = 0
        minbuy = float("inf")
        for price in prices:
            minbuy = min(minbuy, price)
            maxprofit = max(maxprofit, price - minbuy)
        return maxprofit
        
maxprofit = Solution().maxProfit
assert maxprofit([7, 3, 2, 3, 9, 0, 6, 3]) == 7
assert maxprofit([7, 3, 2, 3, 9, 0, 6, 9, 3]) == 9