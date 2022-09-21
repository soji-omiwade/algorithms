from typing import List
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def helper(n,m=0):
            if n==0 and m==0:
                return 1
            if n<0 or m<0:
                return 0
            return helper(n-1,m+1) + helper(n,m-1)
            
        if n < 0:
            raise Exception("n needs to be +ve")
        if n == 0:
            return 0
        return helper(n)
        
assert Solution().generateParenthesis(1) == 1
assert Solution().generateParenthesis(2) == 2
assert Solution().generateParenthesis(3) == 5
