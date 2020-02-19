class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        hlen,nlen=len(haystack),len(needle)
        base=128
        nval=hval=0
        for nch,hch in zip(needle,haystack):
            nval=base*nval+ord(nch)
            hval=base*hval+ord(hch)
            
        if nval==hval:
            return 0
            
        for i in range(1,hlen-nlen+1):
            hval-=ord(haystack[i-1])*(base**(nlen-1))
            hval*=base
            hval+=ord(haystack[i+nlen-1])            
            if nval==hval:
                return i

        return -1
import sys
print(Solution().strStr(sys.argv[1], sys.argv[2]))