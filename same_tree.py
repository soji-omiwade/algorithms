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
        qlevel = deque(q)
        while plevel and qlevel:
            for _ in range(len(plevel)):
                pnode = plevel.popleft()
                qnode = qlevel.popleft()
                
                if bool(pnode.left) ^ bool(qnode.left):
                    return False
                if pnode.left:
                    if pnode.left.val != qnode.left.val:
                        return False
                    plevel.append(pnode.left)
                    qlevel.append(qnode.left)
                if bool(pnode.right) ^ bool(qnode.right):
                    return False
                if pnode.right:
                if pnode.right and pnode.right.val != qnode.right.val:
                    return False
        if bool(plevel) ^ bool(qlevel):
            return False
        return True