class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs_helper(v, p, q):
            leftcount = rightcount = 0
            resleft = resright = None
            selfcount = int(v in (p,q))
            if v.left:
                leftcount, resleft = dfs_helper(v.left, p, q)
            if v.right:
                rightcount, resright = dfs_helper(v.right, p, q)
            res = None
            if selfcount + leftcount + rightcount == 2:
                if selfcount == 1 or (leftcount == rightcount == 1):
                    res = v
            return (selfcount + leftcount + rightcount, 
                    resleft or resright or res)
        if p is q:
            return p
        return dfs_helper(root, p, q)[1]
        
n10 = Node(10)
n6 = Node(6)
n3 = Node(3, n6, Node(7,None,n10))
n9 = Node(9)
n5 = Node(5, Node(8), n9)
n4 = Node(4)
n2 = Node(2, n4, n5)
n1 = Node(1, n2, n3)
assert Solution().lowestCommonAncestor(n1, n3, n10) == n3
assert Solution().lowestCommonAncestor(n1, n9, n6) == n1
assert Solution().lowestCommonAncestor(n1, n4, n9) == n2
assert Solution().lowestCommonAncestor(n1, n5, n5) == n5