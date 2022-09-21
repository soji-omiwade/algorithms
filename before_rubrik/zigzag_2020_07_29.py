class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        aux = [[] for _ in range(numRows)]
        step = 1
        count = 0
        for i in range(len(s)):
            aux[count].append(s[i])
            if (count, step) == (0, -1) or (count, step) == (numRows-1, 1):
                step *= -1
            count += step
        aux2 = []
        for subaux in aux:
            aux2.extend(subaux)
        return ''.join(aux2)
        
convert = Solution().convert
assert convert('paypali', 3) == 'paaplyi'
assert convert('PAYPALISHIRING', 3) == 'PAHNAPLSIIGYIR'
assert convert('PAYPALISHIRING', 1) == 'PAYPALISHIRING'
assert convert('PAYPALISHIRING', 14) == 'PAYPALISHIRING'