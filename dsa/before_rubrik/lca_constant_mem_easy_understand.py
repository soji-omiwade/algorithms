class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs_helper(v: Node) -> tuple:
            """recursive cases: as long as v is not a leaf, look for p and q
            stop immediately i find both p and q in left. 
            otherwise recursively find remaining in right
            """
            left_count = right_count = 0
            if v.left:
                left_count, res_node = dfs_helper(v.left)
                if left_count == 2:
                    return 2, res_node
            if v.right:
                right_count, res_node = dfs_helper(v.right)
                if right_count == 2:
                    return 2, res_node    
            if left_count == right_count == 1:
                return 2, v         
            assert (left_count,right_count) in ((1,0),(0,1),(0,0))
            self_count = int(v.val in (p.val, q.val))
            if left_count + right_count + self_count == 2:
                return 2, v
            "haven't hit the answer, so return None result node"
            assert left_count + right_count + self_count < 2 
            return left_count + right_count + self_count, None

        if p is q: 
            return p
        return dfs_helper(root)[1]

node4 = Node(4)
node5 = Node(5, Node(6), Node(2, Node(7), node4))
node0 = Node(0)
node8 = Node(8)
node1 = Node(1, node0, node8)
root = Node(3, node5, node1)
assert Solution().lowestCommonAncestor(root,node5,node1).val == 3
assert Solution().lowestCommonAncestor(root,node4,node5).val == 5
assert Solution().lowestCommonAncestor(root,node0,node8).val == 1
assert Solution().lowestCommonAncestor(root,node5,node5).val == 5
assert Solution().lowestCommonAncestor(root,root,root).val == 3