'''
have fun!
start: 12:48
end: ...

       3 4 5 0 1 2 | 3 4 5
             z
actual 0 1 2 3 4 5 | 6 7 8

0 + 5
3 + 8  working idxs
mid = 5
shrink until we get the place where there's a gulf: nums[i] < nums[i-1]. res is i
'''
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        '''
        0 1 2 3 4
        1 2 3 4 0  
        '''
        def find_zeroidx(lo, hi):
            while lo < hi:
                mid = (lo + hi) // 2
                if nums[mid] < nums[hi]:
                    hi = mid
                else:
                    lo = mid + 1
            return lo
            
        '''
        3 4 5 | 6 7 8
        
        0 1 2 3 4
        '''
        def conventional_binsearch(lo, hi):
            while lo < hi:
                mid = lo + (hi - lo) // 2
                if nums[mid % len(nums)] < target:
                    lo = mid + 1
                else: # >= 
                    hi = mid
            return -1 if nums[lo % len(nums)] != target else lo % len(nums)
            
        if not nums:
            return -1
        zeroidx = find_zeroidx(0, len(nums) - 1)
        return conventional_binsearch(zeroidx, len(nums) - 1 + zeroidx)
        