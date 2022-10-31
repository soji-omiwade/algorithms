class Solution:
    
    def climbStairs(self, n: int) -> int:
        global foo
        foo = [0] * (n+1)
        def bar(foo, n):
            if n == 0:
                foo[0] = 1
                return 1            
            if n < 0:
                return 0
            #n > 0 and we have memoized
            if foo[n] != 0:
                return foo[n]
            #n > 0 and we haven't memoized
            foo[n] = self.climbStairs(n-2) + self.climbStairs(n-1)
            return foo[n]
        return bar(foo, n)
		
		
		