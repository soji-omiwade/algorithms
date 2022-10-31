class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n=h=0
        #128 assuming ascii
        base=128 
        
        for ch,chp in zip(needle,haystack):
            n=base*n+ord(ch)
            h=base*h+ord(chp)
        
        for i in range(len(haystack)-len(needle)+1):
            if n==h:
                return i
            h -= ord(haystack[i])*pow(base,(len(needle)-1))
            h *= base
            h += ord(haystack[min(i+len(needle),len(haystack)-1)])
        return -1
        
print(Solution().strStr("mississippi","issi"))