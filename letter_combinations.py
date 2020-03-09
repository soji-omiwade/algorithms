from typing import List
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        def foo(digits,curr=None):
            if not digits:
                return
            if not curr:
                curr=[]
            k=len(curr)
            if k==len(digits):
                res.append("".join(curr))
                return
            digit=digits[k]
            chars=d[digit]
            for char in chars:
                foo(digits,curr+[char])
        res=[]
        a=["abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]
        b="23456789"
        d={y:x for x,y in zip(a,b)}
        foo(digits)
        return res
        
assert Solution().letterCombinations("") == []
assert Solution().letterCombinations("2") == ["a","b","c"]
assert Solution().letterCombinations("7") == ["p","q","r","s"]
assert Solution().letterCombinations("23") == ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]