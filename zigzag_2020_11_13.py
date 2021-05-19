from typing import List
from collections import deque
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        q = deque([root])
        isleft = False
        res = []
        while q:
            count = len(q)
            res.append([None] * count)
            for i in range(count):
                node = q.popleft()
                if isleft:
                    i = count - i - 1
                res[-1][i] = node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            isleft = not isleft
        return res

root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
assert Solution().zigzagLevelOrder(root) == [
      [3],
      [20,9],
      [15,7]
    ]