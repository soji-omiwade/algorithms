from typing import List
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def helper(n,res,a,open,close):
            if not close<=open<=n:
                return
            if open+close == 2*n:
                res.append("".join(a))
                return
            helper(n,res,a+["("],open+1,close)
            helper(n,res,a+[")"],open,close+1)
        res=[]
        helper(n,res,[],0,0)
        return res
assert Solution().generateParenthesis(1) == ["()"]
assert sorted(Solution().generateParenthesis(2)) == sorted(["(())","()()"])
assert (sorted(Solution().generateParenthesis(3)) ==
    sorted(["((()))","(()())","(())()","()(())","()()()"]))
