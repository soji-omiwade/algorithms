'''
i/o
arr = [3, 9, 12, 20, 2]
                     ^
target = 11
ans = [2, 9]

arr = [3, 9, 12, 20, 2]
target = 2
ans = null

constraints
-order doesn't matter
-actual values

psuedocode-
i, j: i < j => O(n^2)
method 1: sort the array -> O(n lg n) - time. vs O(n) ? 
method 2: hash set 

'''
from typing import List
def two_sum(arr: List[int], target: int) -> List[int]:
    bag = set()
    for number in arr:
        if target - number in bag:
            return [number, target - number]
        bag.add(number)
    return None
    
arr = [3, 9, 12, 20, 2]
target = 11
ans = [2, 9]
assert two_sum(arr, target) == ans
   
target = 2
ans = None
assert two_sum(arr, target) == ans
target = 42
ans = None
assert two_sum(arr, target) == ans
