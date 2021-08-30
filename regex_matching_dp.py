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
        def helper(si, pi):           
            if pi == len(pattern):
                return si == len(string) 
            
            firstmatches = si < len(string) and pattern[pi] in (".", string[si])
            if pi + 1 < len(pattern) and pattern[pi + 1] == "*":
                if helper(si, pi + 2):
                    return True
                if firstmatches and helper(si + 1, pi):
                    return True
            return firstmatches and helper(si + 1, pi + 1)
        
        return helper(0, 0)
        
        
        