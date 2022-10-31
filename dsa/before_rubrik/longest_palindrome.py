'''
input/output


dccaccd -> number of pairs of same character you can take out
if somethings (that are not pairs) left then
    add 1

build a counter from the string
go through and add to an aggregrate the val count // 2

----
'''
from collections import Counter
class Solution:
    def longestPalindrome(self, s: str) -> int:
        res = 0
        count_one_exists = 0
        for ch, count in Counter(s).items():
            res += 2 * (count // 2)
            if count % 2 == 1:
                count_one_exists = 1
        return res + count_one_exists