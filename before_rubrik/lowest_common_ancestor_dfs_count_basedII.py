class Node:
    def __init__(self, val, left=None, right=None):
        self.left = left
        self.val = val
        self.right = right
    def __str__(self):
        return str(self.val)
def lca(a: Node, b: Node, root: Node) -> Node:
    def dfs_helper(v):
        if v is None:
            return 0, None
        vcount = int(v.val in (a.val, b.val))
        lcount, lres = dfs_helper(v.left)
        rcount, rres = dfs_helper(v.right)
        if (lcount,vcount,rcount) in ((0,1,1),(1,0,1),(1,1,0)):
            return 2, v
        if lcount == 2 or rcount == 2:
            return 2, lres or rres
        if (lcount,vcount,rcount) in ((0,0,1),(0,1,0),(1,0,0)):
            return 1, None
        assert lcount+rcount+vcount == 0
        return 0, None
    return dfs_helper(root)[1]
    
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