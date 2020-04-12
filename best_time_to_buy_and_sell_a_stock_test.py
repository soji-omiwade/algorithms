from best_time_to_buy_and_sell_a_stock import Solution

prices = [7,1,5,3,6,4]
assert Solution().maxProfit(prices) == 5
prices = [7,0,5,3,6,4,1,5,3,6,4]
assert Solution().maxProfit(prices) == 6
prices = [7,6,5,4,3]
assert Solution().maxProfit(prices) == 0
prices = [2,2,2,2,2]
assert Solution().maxProfit(prices) == 0
prices = []
assert Solution().maxProfit(prices) == 0

prices = [7,1,5,3,6,4]
assert Solution().maxProfitDP(prices) == 5
prices = [7,0,5,3,6,4,1,5,3,6,4]
assert Solution().maxProfitDP(prices) == 6
prices = [7,6,5,4,3]
assert Solution().maxProfitDP(prices) == 0
prices = [2,2,2,2,2]
assert Solution().maxProfitDP(prices) == 0
prices = []
assert Solution().maxProfitDP(prices) == 0
