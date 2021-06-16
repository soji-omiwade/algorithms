from collections import defaultdict
from typing import List
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """n=len(strs) m=max(len(s)) for all s in strs
            
        time:n * m lg m
        space:O(mk) even excluding return value because of the dict's keys
        and in case every s is a unique anagram
        """
        d=defaultdict(list)
        for x in strs:
            d[tuple(sorted(x))].append(x)
        return d.values()

sample_list = ["eat", "tea", "tan", "ate", "nat", "bat"]
expectedsol = [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]
mysol = Solution().groupAnagrams(sample_list)
#Hmm...
#I don't think you need to make a tuple 
assert sorted(mysol) == sorted(expectedsol)
