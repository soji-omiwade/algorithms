'''
start: 7:58
end: 8:11
13 mins
constraint:
|nodes| > 0
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        maxdiam = 0
        def helper(curr: TreeNode) -> int:
            nonlocal maxdiam
            if not curr:
                return 0
            leftdepth = helper(curr.left)
            rightdepth = helper(curr.right)
            maxdiam = max(maxdiam, leftdepth + rightdepth)
            return 1 + max(leftdepth, rightdepth)
        
        helper(root)
        return maxdiam
