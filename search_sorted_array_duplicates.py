class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        '''
        start: 1:18am
        end: 1:48 STOP. TIME UP!
        1. split the arr @ middle [one will be sorted and the other wont be!]
            if target falls in range of the sorted binary search for target!. and then return T/F depending on whether it is found
            otherwise, break array into two and again look for target in the sorted array
         
target = 6.5
[4,5,6,6,7,7,1, 2,  4,4  ]  
 0 1 2 3 4 5 6  7 8 9
 
 [2,5,6,0,0,1,2]
  0 1 2 3 4 5 6 
  
[1,0,1,1,1]
 0 1 2 3 4
0
        '''
        def binsearch(lo, hi):
            while lo <= hi:
                mid = lo + (hi - lo) // 2
                if nums[mid] == target:
                    return True
                if nums[mid] > target:
                    hi = mid - 1
                else:
                    lo = mid + 1
            return False
        
        n = len(nums)
        lo, hi = 0, n - 1
        while lo <= hi: 
            mid = lo + (hi - lo) // 2       # 3
            if nums[lo] <= nums[mid]:
                if nums[lo] <= target <= nums[mid]:
                    return binsearch(lo, mid)
                lo = mid + 1
            else: #a[mid] <= a[hi]
                if nums[mid] <= target <= nums[hi]:
                    return binsearch(mid, hi)
                hi = mid - 1
        