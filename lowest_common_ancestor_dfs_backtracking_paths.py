class Node:
    def __init__(self, val, left=None, right=None):
        self.left = left
        self.val = val
        self.right = right
    def __str__(self):
        return str(self.val)
def lca(a: Node, b: Node, root: Node) -> Node:
    def dfs_helper(v, x, px):
        if v is None:
            return
        px += [v]
        dfs_helper(v.left, x, px)
        dfs_helper(v.right, x, px)
        if px[-1] is v and v is not x:
            px.pop()
        
    pa = []
    pb = []
    dfs_helper(root, a, pa)
    dfs_helper(root, b, pb)
    for v, vp in zip(pa, pb):
        if v is not vp:
            break
        res = v
    return res
    
n3 = Node(3)
n2 = Node(2)
n1 = Node(1, n2, n3)
try:
    assert lca(n2, n3, n1) is n1
except:
    print(lca(n2, n3, n1))
assert lca(n2, n1, n1) is n1
n2.right = n4 = Node(4)
assert lca(n4, n3, n1) is n1
n2.left = n5 = Node(5)
assert lca(n5, n4, n1) is n2