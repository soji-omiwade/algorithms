class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        "ppr = path from p to root"
        "pqr = path from q to root"
        def dfs_key_to_v(key, v):
            if v is key:
                return [v]
            if v.left:
                path = dfs_key_to_v(key, v.left)
                if path:
                    return path + [v]
            if v.right:
                path = dfs_key_to_v(key, v.right)
                if path:
                    return path + [v]
            return None
        
        ppr = dfs_key_to_v(p, root)
        pqr = dfs_key_to_v(q, root)
        for v, w in zip(reversed(ppr), reversed(pqr)):
            if v is w:
                res = v
            else:
                break
        return res
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