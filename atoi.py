class Solution:
    def myAtoi(self, s: str) -> int:
        i=0
        while i<len(s) and s[i] in (" ","\t"):
            i+=1
        #now i is at a number, a +/-, or the end of the string
        if i == len(s):
            return 0
            
        is_neg = 1
        if s[i] == "+" or s[i] == "-":
            if s[i] == "-":
                is_neg = -1
            i+=1
        j=i    
        while j<len(s) and ord("0") <= ord(s[j]) <= ord("9"):
            j+=1
        #now j is at a character not numeric
        s = s[i:j]
        
        if len(s) == 0: 
            return 0
          
        minn,maxx=-pow(2,31),pow(2,31)-1
        val = 0
        for ch in s:
            val*=10
            val+=ord(ch)-ord("0")
            if is_neg * val < minn:
                return minn
            if is_neg * val > maxx:
                return maxx
        return is_neg * val
        
print(Solution().myAtoi("   -42dfdf"))