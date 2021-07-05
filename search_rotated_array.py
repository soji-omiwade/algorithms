'''
start: 9:49pm
end:  10:24pm
duration: 45 mins!

constraints:
. nums unique elements

        0 1 2 3 4 5 6
nums = [4,5,6,7,0,1,2], target = 0
                l m h
        
nums = [1,0,2], target = 3
        0 1
        3,1
        l h
        m
        
        0  1  2
        5, 1, 3
           h
           l,m
approach
'''
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binsearch(lo, hi):
            assert lo <= hi
            while lo <= hi:
                mid = lo + (hi - lo) // 2
                if nums[mid] == target:
                    return mid
                if nums[mid] < target:
                    lo = mid + 1
                else:
                    hi = mid - 1
            return -1
        
        lo, hi = 0, len(nums) - 1
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if nums[lo] <= nums[mid]:
                idx_found = binsearch(lo, mid)
                if idx_found >= 0:
                    return idx_found
                lo = mid + 1
            else:  #-> right side is sorted
                idx_found = binsearch(mid + 1, hi)
                if idx_found >= 0:
                    return idx_found
                hi = mid
        return -1
