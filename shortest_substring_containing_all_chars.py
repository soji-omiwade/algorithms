'''
a b c
2 3 1

iterate through each j
    if string[j] in need:
        have[string[j]] += 1
        if have[string[j]] == need[string[j]]:
            count += 1
        
    while count == len (need)
        update maximum wrt i & j
        if string[i] in needset
            count[string[i]] -= 1
            if have[string[i]] < need[string[i]]
                count -= 1
        i += 1
'''
from collections import Counter
from typing import List
def shortest(string: str, chars: List[str]) -> str:
    i = 0
    bestlo, besthi = 0, len(string) - 1
    need = Counter(chars)
    have = Counter()
    count = 0
    for j in range(len(string)):
        if string[j] in need:
            have[string[j]] += 1
            if have[string[j]] == need[string[j]]:
                count += 1
            
        while count == len(need):
            if j - i < besthi - bestlo:
                bestlo, besthi = i, j
            if string[i] in need:
                have[string[i]] -= 1
                if have[string[i]] < need[string[i]]:
                    count -= 1
            i += 1
    return string[bestlo:besthi + 1]
s = "abracadabra"
chars = ['a', 'b']
print(shortest(s, chars)) # ab

chars = ['a', 'b', 'c']
print(shortest(s, chars)) # brac

chars = ['a', 'b', 'c', 'a']
print(shortest(s, chars)) # abrac
