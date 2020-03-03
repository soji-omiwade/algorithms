from typing import List
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def helper(n,res,m,a)->None:
            if n==0 and m==0:
                res.append("".join(a))
            elif n>=0 and m>=0:    
                helper(n-1,res,m+1,a+["("]) 
                helper(n  ,res,m-1,a+[")"])
        #end func
        if n==0:
            return [""]
        res=[]
        helper(n,res,0,[])
        return res
        
assert Solution().generateParenthesis(1) == ["()"]
assert Solution().generateParenthesis(2) == ["(())","()()"]
assert (sorted(Solution().generateParenthesis(3)) ==
    sorted(["((()))","(()())","(())()","()(())","()()()"]))
