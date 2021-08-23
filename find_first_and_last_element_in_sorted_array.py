'''
120pm
1 1 1 2 3 4 5 8 8 |8| 8 8 8 9 10 11
4 |5| 6 |8| 8 8 |8| 8 8 8 9 10 11
6 |8| 8 8 |8| 8 8 8 9 10 11
lo hi

got it. but will do search sorted array after this! definitely 2nite!

for lo-side
    bin-search until you find a | target such that a != target 
for hi-side
    bin-search until you find target | a such that a != target 
res == the target idxs resp.

1 1 2 
target = 2
lo = 0; hi = 2
mid = 1
lo = 2

2      2      2
lo,hi

                if nums[mid] == target and nums[mid - 1] != target:
                    return mid

1    2
lo   hi
mid
                        found
1 2 2 2 2 2 3        4 5 6 7 8 8 8 

lo  hi
2   3

l   h
2 3 8


          l h
2 5 7 8 8 8 12
'''
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def find_lo_idx(lo, hi):
            assert nums[hi] == target
            while lo < hi:
                mid = lo + (hi - lo) // 2
                if nums[mid] != target:
                    if nums[mid + 1] == target:
                        return mid + 1
                    lo = mid + 1
                else:
                    hi = mid
                return lo
        
        def find_hi_idx(lo, hi):
            from  math import ceil
            assert nums[lo] == target
            while lo < hi:
                mid = ceil(lo + (hi - lo) // 2)
                if nums[mid] != target:
                    if nums[mid - 1] == target:
                        return mid - 1
                    hi = mid - 1
                else:
                    lo = mid
            return lo
        
        lo, hi = 0, len(nums) - 1
        lores = hires = -1
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if nums[mid] == target:
                lores = find_lo_idx(lo, mid)
                hires = find_hi_idx(mid, hi)                
            elif nums[mid] < target:
                lo = mid + 1
            else:
                hi = mid - 1
        return [lores, hires]
