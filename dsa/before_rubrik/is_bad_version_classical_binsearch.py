# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):
'''
1 2 3 4 5
F F F T T
ans = 4

1 2 3 4 5
T T T T T
ans = 1

1 2 3 4 5
F F F F F
ans = None

f f hmm.. two calls kind of a waste
f t <--break!
t t hmm.. two calls kind of a waste
'''
class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        lo, hi = 1, n
        res = None
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if isBadVersion(mid):
                res = mid
                hi = mid - 1
            else:
                lo = mid + 1
        return res
            
            