class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None
        if p is q:
            return p
        def dfs_counter(v, p, q):
            selfcount = int(v in (p, q))
            leftcount = rightcount = 0
            resleft = resright = resself = None
            if v.left:
                resleft, leftcount = dfs_counter(v.left, p, q)
            if v.right:
                resright, rightcount = dfs_counter(v.right, p, q)
            if selfcount + rightcount + leftcount == 2:
                if (rightcount == leftcount) or selfcount == (rightcount + leftcount):
                    if rightcount == leftcount:
                        assert rightcount == 1
                    if selfcount == (rightcount + leftcount):
                        assert rightcount == 1 or leftcount == 1
                    resself = v                    
            return resleft or resright or resself, selfcount + rightcount + leftcount
        return dfs_counter(root, p, q)[0]
        
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