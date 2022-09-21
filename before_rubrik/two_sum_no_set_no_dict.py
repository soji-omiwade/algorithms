class Solution:
    def twoSum(self, b: List[int], target: int) -> List[int]:
        a=sorted(b)
        i,j=0,len(a)-1
        while i<j:
            x=a[i]+a[j]
            if x==target:
                y,z=a[i],a[j]
                break
            elif x<target:
                i+=1
            else:
                j-=1
        res=[]
        for i in range(len(b)):
            if b[i] in (y,z):
                res.append(i)
        return res