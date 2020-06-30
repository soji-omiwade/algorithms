class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        res = [[] for _ in range(numRows)]
        index, step = 0, 1
        for ch in s:
            res[index].append(ch)
            if index == 0:
                step = 1
            elif index == numRows - 1:
                step = -1
            index += step
        return "".join("".join(res[i]) for i in range(numRows))
            

def test():
    s="PAYPALISHIRING"
    res = Solution().convert(s,3)
    assert res == "PAHNAPLSIIGYIR"
    res = Solution().convert(s,4)
    assert res == "PINALSIGYAHRPI"
    res = Solution().convert(s,1)
    assert res == s
    res = Solution().convert(s,len(s))
    assert res == s
    
test()