# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []        
        def helper(v,depth):
            if len(res)==depth:
                res.append([])
            res[depth].append(v.val)
            if v.left:
                helper(v.left,depth+1)
            if v.right:
                helper(v.right,depth+1)
        res=[]
        helper(root,0)
        return res