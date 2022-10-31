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
                for val in inorder(curr.left):
                    yield val
                yield curr.val
                for val in inorder(curr.right):
                    yield val
            
        def reverse_inorder(curr):
            if curr:
                for val in reverse_inorder(curr.right):
                    yield val
                yield curr.val
                for val in reverse_inorder(curr.left):
                    yield val
                
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
        