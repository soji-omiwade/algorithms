'''
[5,7,7,8,8,10]
'''
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def losearch(lo, hi):
            while lo < hi:
                mid = (lo + hi) // 2
                if nums[mid] < target:
                    lo = mid + 1
                else: # >= 
                    hi = mid
            return -1 if  not 0 <= lo <= hi or nums[lo] != target else lo            
                
        def hisearch(lo, hi):
            while lo < hi:
                mid = (lo + hi) // 2 + 1
                if nums[mid] > target:
                    hi = mid - 1
                else:
                    lo = mid
            return -1 if  not 0 <= lo <= hi or nums[lo] != target else lo            
            
        loidx = losearch(0, len(nums) - 1)
        hiidx = hisearch(0, len(nums) - 1)
        return [loidx, hiidx]