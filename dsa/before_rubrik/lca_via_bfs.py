class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None
        def get_parents(root):
            from collections import deque
            nodes = deque()
            nodes.append(root)
            parents = {root:None}
            while nodes:
                v = nodes.popleft()
                if v.left:
                    parents[v.left] = v
                    nodes.append(v.left)
                if v.right:
                    parents[v.right] = v
                    nodes.append(v.right)
            return parents
        parents = get_parents(root)
        def get_path(parents, v):
            while v:
                yield v
                v = parents[v]
        ppath = reversed(list(get_path(parents, p)))
        qpath = reversed(list(get_path(parents, q)))
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