'''
    [7,  1, 3,  2, 5,  4]
    [0, -6, 2, -1, 3, -1]
ans = 2 + -1 + 3 = 4
'''
from typing import List
def maxsum(arr: List[int]) -> int:
    derarr = [0]
    for i in range(1, len(arr)):
        derarr.append(arr[i] - arr[i-1])
    maxsum = float("-inf")
    currsum = 0
    for val in derarr:
        currsum = max(0, val + currsum)
        maxsum = max(currsum, maxsum)
    return maxsum

arr = [7,  1, 3,  2, 5,  4]
print(maxsum(arr))    
