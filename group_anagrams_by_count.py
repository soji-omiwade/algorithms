from typing import List
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """complexity; n=len(strs);k=max(len(word),k) for word in strs
            
        time: nk
        """
        from collections import defaultdict
        d=defaultdict(list)
        for word in strs:
            t=[0]*26
            for ch in word:
                t[ord(ch)-ord("a")]+=1
            d[tuple(t)].append(word)
        return d.values()
        
print(list(
    Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])))
    
strs = ["ddg", "dg"]
sol = Solution().groupAnagrams(strs)
print(list(sol))
assert list(sol) == [["ddg"], ["dg"]]