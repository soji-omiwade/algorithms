'''
    5
   / \
  3   6
target = 9
    1
target = 2
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    vals = set()
    def findTarget(self, root: TreeNode, k: int) -> bool:
        if not root:
            return False
        me = (k - root.val in self.vals)
        self.vals.add(root.val)
        return self.findTarget(root.left, k) or me or self.findTarget(root.right, k)
