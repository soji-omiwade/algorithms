"""
Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
"""
from typing import List
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict
        d=defaultdict(list)
        for s in strs:
            d[tuple(sorted(s))].append(s)
        res=[]
        for k,v in d.items():
            res.append(v)
        return res
        
print((sorted(Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))))
assert (sorted(Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])) ==
sorted([
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
])
)