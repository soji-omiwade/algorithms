# Definition for a binary tree TreeNode.
class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right
        
    def __str__(self):
        return str(self.val) + ": " + super().__str__()
    
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(v, p, q, needed=2):
            if not v or not needed:
                return 0, None
            herecount = int(v in (p, q))
            leftcount, resleft = dfs(v.left, p, q, needed - herecount)
            rightcount, resright = dfs(v.right, p, q, needed - herecount - leftcount)
            allcount = herecount + leftcount + rightcount
            res = None
            if 2 in (leftcount, rightcount):
                res = resleft or resright
            elif allcount == 2:
                res = v
            return allcount, res                
            
        return dfs(root, p, q)[1]
        
n10 = TreeNode(10)
n6 = TreeNode(6)
n3 = TreeNode(3, n6, TreeNode(7,None,n10))
n9 = TreeNode(9)
n8 = TreeNode(8)
n5 = TreeNode(5, n8, n9)
n4 = TreeNode(4)
n2 = TreeNode(2, n4, n5)
n1 = TreeNode(1, n2, n3)
assert Solution().lowestCommonAncestor(n5, n8, n9) is n5
assert Solution().lowestCommonAncestor(n3, n3, n10) is n3
assert Solution().lowestCommonAncestor(n1, n3, n10) is n3
assert Solution().lowestCommonAncestor(n1, n9, n6) is n1
assert Solution().lowestCommonAncestor(n1, n4, n9) is n2