class Solution:
    def compareVersion(self,s,s2):
        v1=s.split(".")
        v2=s2.split(".")
        for i in range(max(len(v1),len(v2))):
            x = int(v1[i]) if i < len(v1) else 0
            y = int(v2[i]) if i < len(v2) else 0
            if x > y:
                return 1
            if x < y:
                return -1
        return 0
                
    
assert Solution().compareVersion("0.1","1.1") == -1
assert Solution().compareVersion("1.0.1","1") == 1
assert Solution().compareVersion("7.5.2.4","7.5.3")==-1
assert Solution().compareVersion("1.01","1.001")==0
assert Solution().compareVersion("1.0","1.0.0")==0
assert Solution().compareVersion("1.1","1.10")==-1
assert Solution().compareVersion("1.2","1.10",)==-1