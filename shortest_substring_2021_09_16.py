'''
lo = 0
minlo, minhi = 0, float("inf")
for hi in [0, len(s))
    while window lo-hi has_all_needed_chars
      adjust minlen if need be
      lo += 1
return s[minlo:minhi+1]
'''
from typing import List
from collections import Counter
def shortest_substring(s: str, chars: List[str]) -> str:
    lo = 0
    minlo, minhi = 0, float("inf")
    need = Counter(chars)
    have = Counter()
    for hi, ch in enumerate(s):
        if ch in need:
            have[ch] += 1
        while len(have) == len(need):
          if hi - lo < minhi - minlo:
            minlo, minhi = lo, hi
          if s[lo] in need:
            have[s[lo]] -= 1
            if have[s[lo]] == 0:
                have.pop(s[lo])
          lo += 1
    return s[minlo:minhi+1]
    
s = "abracadabra"
chars = ['a', 'b']
print(shortest_substring(s, chars)) # ab

chars = ['a', 'b', 'c']
print(shortest_substring(s, chars)) # brac

chars = ['a', 'b', 'r']
print(shortest_substring(s, chars)) # abr

chars = ['a', 'c', 'd']
print(shortest_substring(s, chars)) # cad
