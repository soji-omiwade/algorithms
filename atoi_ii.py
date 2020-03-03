class Solution():
    def myAtoi(self, s: str) -> int:
        for i in range(len(s)):
            if s[i] != " ":
                break
        else:
            return 0
        is_neg=1
        if s[i]=="-":
            is_neg=-1
            i+=1
        #now i stands on a non-space non-neg (perhaps...)
        j=i
        while j < len(s):
            if not ord("0")<=ord(s[j])<=ord("9"):
                break
            j+=1
            
        res=0
        for k in range(i,j):
            res=10*res+ord(s[k])-ord("0")
        return res*is_neg
assert Solution().myAtoi("    ") == 0
assert Solution().myAtoi("  words") == 0
assert Solution().myAtoi("  4193 with words") == 4193
assert Solution().myAtoi("  -42 with words") == -42
assert Solution().myAtoi("  -42Fwith words") == -42