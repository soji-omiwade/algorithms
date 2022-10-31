'''
10:28am -- 10:58am
0 1 2 3 4 5
a b c 
a h b g d c b

tlookup[a] = [0]
tlookup[b] = [2, 6]
bigger --> [2] 4?

k * (|s| + |t|)
|t| + (k |s| log |s and t|)

preprocess t, so that we have tlookup[char in t] = list of the locations of those chars

lastloc = 0
for each i, ch in s
    if ch doesn't exist in tlookup then return False
    position = binary search in tlookup[ch] passing lastloc 
     ---> if position == len(tlookup[ch]) return False
    lastloc = tlookup[ch][position] + 1
return True

constraints
- the alphabet size is 26
'''
from bisect import bisect_left
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        #preprocess t, so that we have tlookup[char in t] = list of the locations of those chars
        lookup = [[] for _ in range(26)]
        for idx, ch in enumerate(t):
            lookup[ord(ch) - ord('a')].append(idx)
        lastloc = 0
        for idx, ch in enumerate(s):
            ch_list = lookup[ord(ch) - ord('a')]
            pos = bisect_left(ch_list, lastloc)
            if pos == len(ch_list):
                return False
            lastloc = ch_list[pos] + 1
        return True
