from collections import deque
from typing import List
from tree_builder import build_tree
from treenode import TreeNode
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        """we use a helper to bfs down the tree, checking for
        validity down through for the entire level before moving down to the 
        the next
        """
        def dfs_helper(v, w):
            if v is w is None:
                return True
            if not all([v,w]):
                return False
            if v.val == w.val:
                return (dfs_helper(v.left, w.right) 
                        and dfs_helper(v.right, w.left))
        return dfs_helper(root, root)
assert Solution().isSymmetric(None)
tree = build_tree([2,1,1,4,8,8,4])
assert Solution().isSymmetric(tree)
tree = build_tree([2,1,1,4,8,3,4])
assert not Solution().isSymmetric(tree)
tree = build_tree([2,1,1,4,None,8,4])
assert not Solution().isSymmetric(tree)
