class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        """
        7.5.3
        7.5.3.4
        """
        
        a=version1.split(".")
        b=version2.split(".")
        for x,y in zip(a,b):
            x,y=int(x),int(y)
            if x>y:
                return 1
            if x<y:
                return -1
        if len(a)==len(b):
            return 0
        longer,shorter=a,b
        if len(a)<len(b):
            longer,shorter=b,a
        for i in range(len(shorter),len(longer)):
            if int(longer[i])!=0:
                if longer == a:
                    return 1
                return -1
        return 0
assert Solution().compareVersion("0.1","1.1") == -1
assert Solution().compareVersion("1.0.1","1") == 1
assert Solution().compareVersion("7.5.2.4","7.5.3")==-1
assert Solution().compareVersion("1.01","1.001")==0
assert Solution().compareVersion("1.0","1.0.0")==0
assert Solution().compareVersion("1.1","1.10")==-1
assert Solution().compareVersion(
"1.2",
"1.10",)==-1