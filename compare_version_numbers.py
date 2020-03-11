class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        """
        753
        7534
        """
        def strip_zeros(s):
            """1.0001.00001->1.1.1"""
            """1->1"""
            """1.10->1.10"""
            res=""
            start=0
            done = False
            while not done:
                end=s.find(".",start)
                if end == -1:
                    done = True
                    end=len(s)
                num=int(s[start:end])
                res += str(num)
                if not done:
                    res+="."
                    start=end+1
            return res
        version1=strip_zeros(version1)
        version2=strip_zeros(version2)
        for a,b in zip(version1, version2):
            if a > b:
                return 1
            if a < b:
                return -1
        if len(version1)==len(version2):
            return 0
        if len(version1)>len(version2):
            longer,shorter=version1,version2
        else:
            longer,shorter=version2,version1
        if longer[len(shorter)] != ".":
            if version1 == longer:
                return 1
            return -1
        for i in range(len(shorter),len(longer)):
            ch=longer[i]
            if ch != "." and ch != "0":
                if version1 == longer:
                    return 1
                return -1
        return 0
assert Solution().compareVersion("0.1","1.1") == -1
assert Solution().compareVersion("1.0.1","1") == 1
assert Solution().compareVersion("7.5.2.4","7.5.3")==-1
assert Solution().compareVersion("1.01","1.001")==0
assert Solution().compareVersion("1.0","1.0.0")==0
assert Solution().compareVersion("1.1","1.10")==-1
