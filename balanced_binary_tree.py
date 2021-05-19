# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def height(root):
            if root is None:
                return -1, True
            leftheight, isbal_left = height(root.left)
            if not isbal_left:
                return None, False
            rightheight, isbal_right = height(root.right)
            if not isbal_right:
                return None, False
            return (1 + max(leftheight, rightheight), abs(leftheight - rightheight) < 2)
    
        return height(root)[1]


def height(node: TreeNode) -> int:
    if node is None:
        return -1
    return 1 + max(height(node.left), height(node.right))

depth(node, root, 0)

def depth(node: TreeNode, curr: TreeNode, depth) -> int:
    if curr is None:
        return -1
    if curr is node:
        return depth
    res = depth(node, curr.left, depth + 1)
    if res != -1:
        return res
    return depth(node, curr.right, depth + 1)