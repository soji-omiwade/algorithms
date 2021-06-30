# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        def inorder(curr):
            if curr:
                yield from inorder(curr.left)
                yield curr.val
                yield from inorder(curr.right)
            
        def reverse_inorder(curr):
            if curr:
                yield from reverse_inorder(curr.right)
                yield curr.val
                yield from reverse_inorder(curr.left)
                
        inorder_gen = inorder(root)
        reverse_gen = reverse_inorder(root)
        
        
        left = next(inorder_gen)
        right = next(reverse_gen)
        while True:
            if left == right:
                return False
            if left + right == k:
                return True
            if left + right < k:
                left = next(inorder_gen)
            else:
                right = next(reverse_gen)
        