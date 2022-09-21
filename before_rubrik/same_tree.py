#time: 3:52pm  -- 
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        from collections import deque
        pq = deque([p])
        qq = deque([q])
        '''
            2
        1       3
        '''
        while pq:
            pnode = pq.popleft()
            qnode = qq.popleft()
            if pnode is qnode is None:
                continue
            elif not pnode or not qnode:
                return False
            elif pnode.val != qnode.val:
                return False
            pq.append(pnode.left)
            pq.append(pnode.right)
            qq.append(qnode.left)
            qq.append(qnode.right)
        return True

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
