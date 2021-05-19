class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isequal(t1:TreeNode, t2: TreeNode) -> bool:
    if (t1 and not t2) or (t2 and not t1):
        return False
    if t1 is t2 is None:
        return True
    if (t1.val == t2.val 
        and isequal(t1.left, t2.left) 
        and isequal(t1.right, t2.right)
        ):
        return True
        
t1 = TreeNode(5, TreeNode(2), TreeNode(4))
t2 = TreeNode(5, TreeNode(2), TreeNode(42))
assert not isequal(t1, t2)
t2 = TreeNode(5, TreeNode(2), TreeNode(4))
assert isequal(t1, t2)
t1 = TreeNode(5, TreeNode(2, TreeNode(1), TreeNode(0)), TreeNode(4))
t2 = TreeNode(5, TreeNode(2, TreeNode(1), TreeNode(0)), TreeNode(4))
assert isequal(t1, t2)
t2 = TreeNode(5, TreeNode(2), TreeNode(4))
