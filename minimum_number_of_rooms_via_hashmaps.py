from collections import defaultdict
from typing import List

class Solution:
    # @param A : list of list of integers
    # @return an integer
    def solve(self, arr: List[int]):
        d = defaultdict(int)
        for start, end in arr:
            d[start] += 1
            d[end] -= 1
            
        ans = 0
        cnt = 0
        times = sorted(d)
        for t in times:
            # print(t, d[t])
            cnt += d[t]
            ans = max([ans, cnt])
        
        return ans

