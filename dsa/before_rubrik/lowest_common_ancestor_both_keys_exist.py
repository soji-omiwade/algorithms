'''
12:50
        3
    /       \
    5        1
  /   \     /  \
 6     2   0    8
      / \
     7   4
LCA(n3, 5, 4) = n5 
LCA(n3, 5, 0) = n3

if am null return 0
if sum of shored up 

if left or right is 2 return left or right #2,0,0 or 0,0,2
if left + right + me is 2 return urself # any two could be 1
return me + left + right # 1,0,0 or 0,1,0 or 0,0,0

need to account 4 urself...


0) if me is null
        return null
1) if left and right, (left or right) and me return me
2) return left or right


        2
    /       \
   3         8

'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None
        
        me = root if root.val in (p.val, q.val) else None
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if (left and right) or ((left or right) and me):
            return root
        return left or right or me
            
        