from typing import List
#time 9:15pm
#time end 9:34pm
#time compl:
#space compl:
# Definition for a binary tree node.
# 0 1 2 3 4 5 
'''
            2
        0
           1
'''
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        def helper(lo: int, hi: int) -> TreeNode:
            if lo > hi:
                return None
            assert lo <= hi
            mid = lo + (hi - lo) // 2
            tnode = TreeNode(nums[mid])
            tnode.left = helper(lo, mid - 1)
            tnode.right = helper(mid + 1, hi)
            return tnode
            
        if not nums:
            return None
        return helper(0, len(nums) - 1)       
        
res = Solution().sortedArrayToBST([i for i in range(6)])
assert (
    res.val == 2
    and res.left.val == 0
    and res.right.val == 4
    and res.left.left is None
    and res.left.right.val == 1
    )
