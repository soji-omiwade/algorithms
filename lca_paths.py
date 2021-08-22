'''
a-b- c-d-root
    /    /
a2-b2   rootc

    a
   / \
   b   c
'''
class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
def lca(root: TreeNode, one: TreeNode, other: TreeNode):
    def getpaths(curr, node, path):
        if not curr:
            return
        path.append(curr.val)
        res = None
        if curr is node:
            res = path[::-1]
        res = res or getpaths(curr.left, node, path)
        res = res or getpaths(curr.right, node, path)
        path.pop()
        return res
        
    pathone = getpaths(root, one, [])
    pathother = getpaths(root, other, [])
    res = None
    print(pathone, pathother)
    while pathone and pathother and pathone[-1] == pathother[-1]:
        res = pathone.pop()
        pathother.pop()
    return res
    
a2 = TreeNode("a2")
a = TreeNode("a")
c = TreeNode("c", TreeNode("b", a), TreeNode("b2", a2))
root = TreeNode("root", TreeNode("d", c), TreeNode("rootc"))
print(lca(root, a2, a)) # c
print(lca(root, root, a2)) #root