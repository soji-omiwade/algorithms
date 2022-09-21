class Solution:
    def minWindow(self, s: str, t: str) -> str:
        def is_sub(s,p,r,t):
            sp=s[p:r+1]
            for x in t:
                if x not in sp:
                    return False
            return True
        
        p=r=0
        for r in range(len(s)):
            if is_sub(s,p,r,t):
                po,ro=p,r
                break
        else: return ""
        
        while r<len(s):
            p+=1
            while not is_sub(s,p,r,t): p+=1
            while r<len(s) and not is_sub(s,p,r,t): r+=1
            if r!=len(s) and r-p < ro-po:
                po,ro=p,r
        return s[po:ro+1]
        
print(Solution().minWindow("ADOBECODEBANC","ABC"))