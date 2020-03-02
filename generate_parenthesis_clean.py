from typing import List
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        """
        invariant: ccount<ocount<n
        """
        def helper(res,n,a,ocount,ccount):
            if ocount+ccount==2*n:
                res.append("".join(a))
                return
                
            if ccount<ocount:
                helper(res,n,a+[")"],ocount,ccount+1)
            if ocount<n:
                helper(res,n,a+["("],ocount+1,ccount)
        if n==0:
            return [""]
        res=[]
        helper(res,n,[],0,0)
        return res
assert Solution().generateParenthesis(1) == ["()"]
assert sorted(Solution().generateParenthesis(2)) == sorted(["(())","()()"])
assert (sorted(Solution().generateParenthesis(3)) ==
    sorted(["((()))","(()())","(())()","()(())","()()()"]))
