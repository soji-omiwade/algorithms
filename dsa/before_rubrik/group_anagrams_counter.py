'''
cat bat fat tab
[[cat], [bat, tab], [fat]]

----------------

go through each str in strs
    str --> samed--up --> sort
    go through the rest of the strs
        if we find str and strp are the same
            with key str add strp  to res
return res

a b c d a b
^
count[i] += 1


cat bat fat tab
cat => c: 1, a:1, t: 1
result[frozenset(cat)].append(tac)
return list of the result values

make frozenset of cat
append to a list (create list in result mapping)

auto add keys
for each str in strs
    

function(str)
    turns into a frozenset

a[1] 2 ..

"ate"
Counter(a:1)

2) can we do better than quadratic time complexity --> O(n)
1) samed up str  -->
    key -> 

'''

from collections import defaultdict, Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)
        for str_ in strs:
            result[frozenset(Counter(str_).items())].append(str_)
        return list(result.values())