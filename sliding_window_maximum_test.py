from sliding_window_maximum_long import Solution

func = Solution().maxSlidingWindow
assert func([7, 2, 4], 2) == [7, 4]
assert func([1,3,-1,-3,5,3,6,7], 3) == [3,3,5,5,6,7]
assert func([i for i in range(10)], 4) == [i for i in range(3,10)]
print(func([i for i in range(10,0,-1)], 4))
assert func([i for i in range(10,0,-1)], 4) == [i for i in range(10,3,-1)]