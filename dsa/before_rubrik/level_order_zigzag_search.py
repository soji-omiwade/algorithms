from collections import deque
from tree_builder import build_tree
from typing import List
from treenode import TreeNode
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        q=deque()
        q.append(root)
        now_go_right=False
        count=1
        res=[]
        while q:
            res.append([0]*count)
            for i in range(count):
                v = q.popleft()
                x=i
                if now_go_right:
                    x = len(res)-1-i
                res[len(res)-1][x]=v.val
                if v.left:
                    q.append(v.left)
                if v.right:
                    q.append(v.right)
            count = len(q)
            now_go_right = not now_go_right
        return res

tree=build_tree([1,2,3,4,5,7,6])
res=[[1],[3,2],[4,5,7,6]]
assert Solution().zigzagLevelOrder(tree) == res


tree=build_tree([1,2,3,None,5,7,6])
res=[[1],[3,2],[5,7,6]]
assert Solution().zigzagLevelOrder(tree) == res
