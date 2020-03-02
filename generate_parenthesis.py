from typing import List
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def helper(n,res,m=0,a=None,ch=None)->None:
            if a is None:
                a=[]
            
            a.append(ch)    
            if n==0 and m==0:
                res.append("".join(a[1:]))
            elif n>=0 and m>=0:    
                helper(n-1,res,m+1,a,"(") 
                helper(n  ,res,m-1,a,")")
            a.pop()
            
        if n==0:
            return [""]
        res=[]
        helper(n,res)
        return res
        
assert Solution().generateParenthesis(1) == ["()"]
assert Solution().generateParenthesis(2) == ["(())","()()"]
assert (sorted(Solution().generateParenthesis(3)) ==
    sorted(["((()))","(()())","(())()","()(())","()()()"]))
