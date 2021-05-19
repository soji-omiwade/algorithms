from typing import List, Tuple
def go(target: int, arr: List[int]) -> Tuple[int, int]:
    visited = set([])
    idx = {}
    for i in range(len(arr)):
        if target - arr[i] in visited:
            return (i, idx[target - arr[i]])
        visited.add(arr[i])
        idx[arr[i]] = i
retval = go(9, [1, 11, 4, 6, 5, 42])
assert retval == (4,2)
retval = go(10, [1, 11, 5, 4, 6, 42])
assert retval == (4,3)
'''
anxiety reins
distraction reins
'''