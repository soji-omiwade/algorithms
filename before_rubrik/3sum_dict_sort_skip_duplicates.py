'''
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]

sortednums
for each num in this set, num
    -num: find two others that sum to it. such that no idxs are the same
n ^ n
O(1) --> O(n) depending on the sort mechanism

nums
-num: key: lookup[-num - self ]   1 -  -1   not find => you add yourself? 
in order to avoid duplicate issue ==> create set out of setnums
T: O(n * n)
S: set + lookup --> O(n)

constraints
no duplicate triplets
    - if i find triplet ensure that I don't insert it into my result
    - as I advance, I ensure the next will not already exist
    
nums = [-1,0,1,2,-1,-4]
res = []

'''    
#time complexity:
#>>> #append--8720, 8868, 8660
#>>> #set add--8296, 7884, 8032
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        def twosum(firstidx, firstnum): 
            lookup = {}
            thirdidx = 0
            while thirdidx < len(nums):
                if thirdidx != firstidx:
                    thirdnum = nums[thirdidx]
                    secondnum = -firstnum - thirdnum
                    if secondnum in lookup:
                        result.add(tuple(sorted((firstnum, thirdnum, secondnum))))
                        while thirdidx < len(nums) and nums[thirdidx] == thirdnum:
                            thirdidx += 1
                        thirdidx -= 1
                    lookup[thirdnum] = thirdidx
                thirdidx += 1
                
        nums = sorted(nums)
        result = set()
        for firstidx, firstnum in enumerate(nums):
            twosum(firstidx, firstnum)
        return list(result)