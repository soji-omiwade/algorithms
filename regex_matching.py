'''
aab
a.b

aabab
aa

aa
aabab

aaaab
a*b

zero
aaaab
b

or more
aaab
a*b



0: b
1: ab
    

func ismatch(s, p)
    firstmatches = ...
    if p[1] == *
        if ismatch(s, p[2:])
            return True
        if ismatch(s[1:], p[0:])
    else
        return firstmatches and ismatch(s[1:], p[1:])
    
*-case (recursive)
    0 * case 
    try 1 -
no * case
'''
class Solution:
    def isMatch(self, string: str, pattern: str) -> bool:
        if not pattern:
            return not string
        # if not string:
        #     return not pattern
        firstmatches = bool(string) and pattern[0] in (".", string[0])
        
        #s = a, p = a*
        if len(pattern) > 1 and pattern[1] == "*":
            if self.isMatch(string, pattern[2:]):
                return True
            if firstmatches and self.isMatch(string[1:], pattern):
                return True
        return firstmatches and self.isMatch(string[1:], pattern[1:])
        
        
        
        