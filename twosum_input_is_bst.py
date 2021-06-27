'''
if num...if k - num is in lookup
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        def helper(curr: TreeNode) -> bool:
            if not curr:
                return False
            left = helper(curr.left)
            me = k - curr.val in vals
            vals.add(curr.val)
            right = helper(curr.right)
            return left or me or right
        vals = set()
        return helper(root)