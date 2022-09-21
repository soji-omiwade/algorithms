'''
traverse(curr, runningsum) -> bool:
    if not curr
        return False
    if curr is leaf
        return targetSum == val + runningsum
    foundleft = traverse(left, runningsum + curr.val)
    foundright = traverse(right, runningsum + curr.val)
    return foundleft or foundright

hasPathSum
    runningsum = traverse(root)
    return runningsum == targetSum
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        def traverse(curr, runningsum) -> bool:
            if not curr:
                return False
            if curr.left is curr.right is None:
                return targetSum == curr.val + runningsum
            foundleft = traverse(curr.left, runningsum + curr.val)
            foundright = traverse(curr.right, runningsum + curr.val)
            return foundleft or foundright        
        return traverse(root, 0)