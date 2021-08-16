'''
123
3, 2, 1, 

maxint
x = 

543 * 10 > 5436
543  > 5436 // 10 -> 543
543 ok, 544 not ok
problem is if val == 544
'''
class Solution:
    def reverse(self, x: int) -> int:
        ans = 0
        maxint = 2**31 - 1
        sign = 1
        if x < 0:
            sign = -1
            x = -x
        while x:
            rem = x % 10
            x //= 10
            if ans > maxint // 10 or (ans * 10 > maxint - rem):
                return 0
            ans = 10 * ans + rem
        return sign * ans
            