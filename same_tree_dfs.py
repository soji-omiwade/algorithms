# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        return (
            self.isSameTree(p.left, q.left) and
            self.isSameTree(p.right, q.right) and
            p.val == q.val
        )

p = TreeNode(2, TreeNode(1), TreeNode(3))     
q = TreeNode(2, TreeNode(1), TreeNode(3))     
assert Solution().isSameTree(p, q)
p = TreeNode(2, TreeNode(1), TreeNode(3))
q = TreeNode(2, TreeNode(1), TreeNode(4))     
assert not Solution().isSameTree(p, q)
p = TreeNode(2, TreeNode(1), TreeNode(3))
q = TreeNode(2, TreeNode(1, TreeNode(5)), TreeNode(3))     
assert not Solution().isSameTree(p, q)
p = TreeNode(2, TreeNode(1, None, TreeNode(5)), TreeNode(3))
q = TreeNode(2, TreeNode(1, right=TreeNode(5)), TreeNode(3))     
assert Solution().isSameTree(p, q)
