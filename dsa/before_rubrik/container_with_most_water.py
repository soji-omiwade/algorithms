from typing import List
class Solution:
    def maxArea(self, height: List[int]) -> int:
        i,j=0,len(height)-1
        im,jm,mx=0,0,0
        while i<j:
            val = (j-i)*min(height[i],height[j])
            if val > mx:
                im,jm,mx=i,j,val
            if height[i]<height[j]:
                i+=1
            else:
                j-=1
        return mx
print(Solution().maxArea([1,8,6,2,5,4,8,3,7]))