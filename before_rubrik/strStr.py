class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        hlen=len(haystack)
        nlen=len(needle)
        h=n=0
        base=128
        for chh,chn in zip(haystack,needle):
            n=base*n+ord(chn)
            h=base*h+ord(chh)
        for i in range(hlen-nlen+1):
            if n==h:
                return i
            h %= ord(haystack[i])*pow(base,nlen-1)
            h *= base
            h += ord(haystack[min(i+nlen,hlen-1)])
        return -1
assert Solution().strStr("hello", "ll") == 2
assert Solution().strStr("paa","aa") == 1
assert Solution().strStr("mississippi","ip") == 7
assert Solution().strStr("mississippi","issi") == 1