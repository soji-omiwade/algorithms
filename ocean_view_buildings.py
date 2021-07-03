'''
There are n buildings in a line. You are given an integer array heights of size n that represents the heights of the buildings in the line.

The ocean is to the right of the buildings. A building has an ocean view if the building can see the ocean without obstructions. Formally, a building has an ocean view if all the buildings to its right have a smaller height.

Return a list of indices (0-indexed) of buildings that have an ocean view, sorted in increasing order.


start: 10:26 - 10:39


2 3 10 9 4 6   ______
res = [6,9,10]
'''

from typing import List
def oceanviews(heights: List[int]):
    '''
    no need: 
        res.add building[-1]
        for all bui
    '''
    tallest = 0
    res = []
    n = len(heights)
    for idx, height in enumerate(reversed(heights)):
        if height > tallest:
            res.append(n - 1 - idx)
            tallest = max(tallest, height)
    return res[::-1]
    
arr = [2, 3, 10, 9, 4, 6]
print(oceanviews(arr))
arr = [1, 44, 3, 2, 1]
print(oceanviews(arr))
#4, 3, 2, 1, 

