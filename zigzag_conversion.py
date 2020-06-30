class Solution:
    def convert2(self, s: str, numRows: int) -> str:
        n = len(s)
        if numRows == 1:
            return s
        aux = [[] for _ in range(numRows)]
        k = 0; step = 1
        for i in range(n):
            aux[k].append(s[i])
            k += step
            if k in (0, numRows - 1):
                step *= -1
        return "".join(["".join(aux[k]) for k in range(numRows)])
    
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        res = ""
        n = len(s)
        for k in range(numRows):
            i = k
            while i < n:
                res += s[i]
                if k not in (0, numRows - 1) and i+2*numRows-2-2*k < n:
                    res += s[i + 2*numRows - 2 - 2*k]
                i += 2 * numRows - 2
        return res
s = "PAYPALISHIRING"
t = "PAHNAPLSIIGYIR"
try: 
    assert Solution().convert(s, 3) == t
except:
    print(Solution().convert(s, 3))

s = "PAYPALISHIRING"
t = "PAYPALISHIRING"
assert Solution().convert(s, 1) == s


s = "PAYPALISHIRING"
t = "PAHNAPLSIIGYIR"
try: 
    assert Solution().convert2(s, 3) == t
except:
    print(Solution().convert2(s, 3))

s = "PAYPALISHIRING"
t = "PAYPALISHIRING"
assert Solution().convert2(s, 1) == s
