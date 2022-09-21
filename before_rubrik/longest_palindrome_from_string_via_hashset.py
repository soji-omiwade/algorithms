'''
aaaabpqqq
expected ans: 6 + 1 = 7
basic idea: 
here x is the set of characters without a match
so we can build a set. and if we add one, we also take one away if we find a match.
then what is left is bpq
the ans is easily then len(s) - count of chars without match.

answer = len(qaaxaaq) = 5 
'''
class Solution:
    def longestPalindrome(self, s: str) -> int:
        matchfinder = set([])
        for ch in s:
            if ch not in matchfinder:
                matchfinder.add(ch)
            else:
                matchfinder.remove(ch)
        return len(s) - len(matchfinder) + int(bool(matchfinder))
        
