'''
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

List[str] -> [[eat, ate, tea], [nat, tan], [bat]]

-------
result = [[eat,tea,ate,], [tan, nat], [bat]]
T:O(n^2 * k^2)

what would be nice?

lookup[eat or ate or tea]

standard(eat, ate) --> sorted

[[sorted(eat): (eat, ate)] ] --> T:O(n * k lg k)

counting sort -> frequency pattern. ate: [1,0,0,0,1,...1/2]

complexity: O(n* alphabet)

function freqpattern(ana)
    t = [26]
    for ch in the ana:
        t[ch - ord(a)] += 1
    return tuple(t)

for each ana in strs
    if freqpattern(ana) not in lookup
        lookup[freqpattern(ana)] = []
    lookup[freqpattern(ana)].add(ana)
    
return lists of the lookup
'''
from collections import defaultdict
class Solution:
    
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def freqpattern(ana):
            pattern = [0] * 26
            for ch in ana:
                pattern[ord(ch) - ord('a')] += 1
            return tuple(pattern)
        
        lookup = defaultdict(list)
        for ana in strs:
            lookup[freqpattern(ana)].append(ana)
        return list(lookup.values())
        