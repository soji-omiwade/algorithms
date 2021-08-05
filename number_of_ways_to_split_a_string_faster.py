'''
relax

io
0 1 2 3 4 5 6 7
1 0 1 1 0  0  0 1 0 0 0 1 1 0 0 0 1 0 1 1
        l1   r1             l2  r2
(leftcount + 1) * (rightcount + 1)
0 1 2 3 4 5 6 7
0 0|0 0|0 0 0 0

1111     1111      1111
                         
constraints/edge cases

pseudocode
three cases
-onecount % 3 != 0 => ans = 0
-onecount == 0 => ans (n-1) choose 2
-else: move bars within boundary
'''
class Solution:
    def getborders(self, s, onecount):
        count = 0
        idx = 0
        while count < onecount // 3:
            if s[idx] == "1":
                count += 1
            idx += 1
        l1 = idx 
        
        assert s[idx] == "0"
        r1 = s.find("1", idx) - 1

        count = 0
        idx = r1 + 1
        while count < onecount // 3:
            if s[idx] == "1":
                count += 1
            idx += 1
        l2 = idx 
        assert s[l2] == "0"
        r2 = s.find("1", l2) - 1
        
        return l1, r1, l2, r2
    
        
        
        
    def numWays(self, s: str) -> int:
        n = len(s)
        onecount = sum(1 if let == "1" else 0 for let in s)
        if onecount % 3 != 0:
            return 0
        if onecount == 0:
            return (n-1) * (n-2) // 2
        l1, r1, l2, r2 = self.getborders(s, onecount)
        return (r1 - l1 + 2) * (r2 - l2 + 2)
        
        
s = "00000"
print(Solution().numWays(s))  #6


s = "0001000101001"
print(Solution().numWays(s))  #0


import re
s = "1 0 1 1 0  0       0 1 0 0 0 1 1 0 000     0 1 0 1 1"
s = re.sub(' +', '', s)
# print(s)
print(Solution().numWays(s)) #16