class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None
        def dfs_path(v, key, path):
            "usage: dfs_path(root, key_node)"
            path += [v]
            if v.left:
                dfs_path(v.left, key, path)
            if v.right:
                dfs_path(v.right, key, path)
            if path[-1] is not key:
                path.pop()
        ppath,qpath = [], []
        dfs_path(root, p, ppath)
        dfs_path(root, q, qpath)
        for v, w in zip(ppath, qpath):
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
assert Solution().lowestCommonAncestor(None, n3, n10) is None