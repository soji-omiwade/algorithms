#time: 3:52pm  -- 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        from collections import deque
        if bool(p) ^ bool(q):
            return False
        plevel = deque(p)
        pcount = qcount = 1
        qlevel = deque(q)
        while plevel or qlevel:
            paux = []
            quax = []
            for _ in range(len(plevel)):
                pnode = plevel.popleft()
                qnode = qlevel.popleft()
                paux.append(node)
                
                plevel.append(node.left)
                plevel.append(node.right)
                
            if paux != qaux or reverse
                return False
        if bool(plevel) ^ bool(qlevel):
            return False
        return True