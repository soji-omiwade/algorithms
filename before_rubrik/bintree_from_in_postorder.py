# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        def helper(iostart, ioend) -> TreeNode:
            nonlocal poidx
            if iostart > ioend:
                return None
            myval = postorder[poidx]
            poidx -= 1
            myidx = inorderidx[myval]
            me = TreeNode(myval)
            me.right = helper(myidx + 1, ioend)
            me.left = helper(iostart, myidx - 1)
            return me
        
        inorderidx = {ioval: idx for idx, ioval in enumerate(inorder)}
        poidx = len(inorder) - 1
        return helper(0, len(postorder) - 1)