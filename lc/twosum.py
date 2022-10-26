'''
indices have to be different
exactly one solution

2 7 11 15
2? 
index = {2:0, }
target = 9
'''
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index = {}
        for idx, val in enumerate(nums): # 0,2; 1,7
            if target - val in index: #2 in index? yes
                return index[target - val], idx
            index[val] = idx
        raise Exception('shouldnt be here')
