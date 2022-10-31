# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, pre: List[int], post: List[int]) -> TreeNode:
        def traverse(curr, val):
            if not curr.left:
                curr.left = TreeNode(val)
            elif postorderidx[val] < postorderidx[curr.left.val]:
                traverse(curr.left, val)
            elif not curr.right:
                curr.right = TreeNode(val)
            else:
                traverse(curr.right, val)
            
        root = TreeNode(pre[0])
        postorderidx = [None] * (1 + len(post))
        for idx, val in enumerate(post):
            postorderidx[val] = idx
        for preidx in range(1, len(pre)):
            val = pre[preidx]
            traverse(root, val)
        return root