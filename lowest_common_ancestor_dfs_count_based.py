from treenode import TreeNode
from tree_builder import build_tree, get_node
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """via a helper that counts p/q and returns the result"""
        def dfs_helper(v: TreeNode) -> TreeNode:
            if not v:
                return 0, None
            count, res = dfs_helper(v.left)
            if count == 2:
                return 2, res
            count2, res = dfs_helper(v.right)
            if count2 == 2:
                return 2, res    
            if count == count2 == 1:
                return 2, v         
            """at this point, i have 1,0 or 0,1 or 0,0 on the kids"""
            count3 = 0
            if v.val in (p.val, q.val):
                count3 = 1
            if count + count2 + count3 == 2:
                return 2, v
            return count + count2 + count3, None
            
        return dfs_helper(root)[1]
tree = build_tree([3,5,1,6,2,0,8,None,None,7,4])
pp,qq=5,1
pp=get_node(tree,pp)
qq=get_node(tree,qq)
assert Solution().lowestCommonAncestor(tree,pp,qq).val == 3
pp,qq=5,4
pp=get_node(tree,pp)
qq=get_node(tree,qq)
assert Solution().lowestCommonAncestor(tree,pp,qq).val == 5