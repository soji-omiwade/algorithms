# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        from math import inf
        def inorder(v, lower=-inf, upper=inf)->bool:
            if v is None:
                return True
            
            if not lower<v.val<upper:
                return False
                
            if not inorder(v.left,lower,v.val):
                return False
            if not inorder(v.right,v.val,upper):
                return False
                
            return True
        
        return inorder(root)
               
               
assert Solution().isValidBST(None)

t=TreeNode(2)
t.left=TreeNode(1)
t.right=TreeNode(3)
assert Solution().isValidBST(t)

t=TreeNode(2)
t.left=TreeNode(11)
t.right=TreeNode(5)
assert not Solution().isValidBST(t)

t=TreeNode(2)
assert Solution().isValidBST(t)

a=[5,1,4,None,None,3,6]
r=TreeNode(a[0]); r.left,r.right=TreeNode(a[1]),TreeNode(a[2])
r.right.left,r.right.right=TreeNode(a[5]),TreeNode(a[6])
assert not Solution().isValidBST(r)

a=[10,5,15,None,None,6,20]
r=TreeNode(a[0]); r.left,r.right=TreeNode(a[1]),TreeNode(a[2])
r.right.left,r.right.right=TreeNode(a[5]),TreeNode(a[6])
assert not Solution().isValidBST(r)


