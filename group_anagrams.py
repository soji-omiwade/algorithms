class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """n=len(strs) m=max(len(s)) for all s in strs
            
        time:n * m lg m
        space:O(mk) even excluding return value because of the dict's keys
        and in case every s is a unique anagram
        """
        from collections import defaultdict
        d=defaultdict(list)
        for x in strs:
            d[tuple(sorted(x))].append(x)
        return d.values()

print(list(
    Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])))