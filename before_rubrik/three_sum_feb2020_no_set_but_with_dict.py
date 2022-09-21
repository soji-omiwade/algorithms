class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res=[]
        
        def two_sum(i,nums):
            foo=set([])
            target=-nums[i]
            d={}
            for j in range(i+1,len(nums)):
                d[target-nums[j]]=j
            for j in range(i+1,len(nums)):
                if nums[j] in d and d[nums[j]] != j:
                    x,y=nums[j],target-nums[j]
                    if x > y:
                        x,y=y,x
                    foo.add((-target,x,y))
            return foo
        
        i=0
        while i < (len(nums)):
            if nums[i]>0:
                break
                
            if i==0 or nums[i] != nums[i-1]:
                res+=list(two_sum(i,nums))
                
            i+=1
        return res
