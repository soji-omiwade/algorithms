'''
t

    b
 3  5
preprocess t so that we have
lookup['b'] --> [2, 5, 9] [all indices of that letter]
lastloc = 3
'''
from collections import defaultdict, deque
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        lookup = defaultdict(deque)
        for ch in t:
            lookup[ch].append(ch)
        lastloc = 0
        for idx, ch in enumerate(s):
            if not lookup[ch]:
                return False
        #no! stop! a deque would be inefficient: have to pop until you find the idx greater than lastloc
        #T: O(|t|)
        