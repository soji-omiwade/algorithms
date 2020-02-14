class Solution:
    def intToRoman(self, num: int) -> str:
        values = (1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1)
        letters = ("M", "CM", "D", "CD", "C", 'XC','L','XL','X','IX','V','IV', 'I')
        res=""
        for i in range(len(values)):
            count = num//values[i]
            res += count*letters[i]
            num%=values[i]
        return res
import sys
print(Solution().intToRoman(int(sys.argv[1])))