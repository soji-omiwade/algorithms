from typing import List
from collections import Counter
class Solution:
    def shortest_substring(self, s:str, arr: List) -> str:
        m, n = len(arr), len(s)
        im, jm = 0, n
        i = 0
        counter = Counter()
        set_arr = set(arr)
        for j in range(n):
            if s[j] in set_arr:
                counter[s[j]] += 1
                while len(counter) == m:
                    if j - i < jm - im:
                        im, jm = i, j
                    if s[i] in counter:
                        counter[s[i]] -= 1
                        if counter[s[i]] == 0:
                            del counter[s[i]]
                    i += 1
        if jm == n:
            return ''
        return s[im:jm+1]
sub = Solution().shortest_substring
print(f"res: {sub('ADOBECODEBANC', ['A', 'B', 'C'])}")
assert sub('ADOBECODEBANC', ['A', 'B', 'C']) == 'BANC'
assert sub('YYrstYewdaYZX', ['X', 'Y', 'Z']) == 'YZX'

