class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        def twoSum(nums: List[int], start: int, res: List[int]) -> List[int]:
            target = nums[start]
            
            
            
            for i in range(start+1, len(nums)):
                if i == start+1 or nums[i] != nums[i-1]:                
                    if nums[i] in d: 
                        dnsi = d[nums[i]]                    
                        if dnsi != i and nums[i] <= nums[dnsi]:
                            res.append((nums[i], nums[dnsi], target))

        a = sorted(nums)
        i = 0
        res = []
        for i in range(len(a)): 
            if i == 0 or a[i] != a[i-1]: 
                twoSum(a,i,res)
        return res