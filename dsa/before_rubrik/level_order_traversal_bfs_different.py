from treenode import TreeNode
from tree_builder import build_tree
# Definition for a binary tree node.
class Solution:
    def levelOrder(self, root):
        """
                        2
                4             8
            5      .       19  10
         13  12          23 24   25
        """
        from collections import deque
        q = deque()
        if root is None:
            return []
        q.append(root)
        count=len(q)
        res=[]
        while q:
            res.append([])
            for i in range(count):
                v = q.popleft()
                res[len(res)-1].append(v.val)
                if v.left:
                    q.append(v.left)
                if v.right:
                    q.append(v.right)
            count = len(q)
        return res
def main():
    tree=[2,4,8,5,None,19,10,13,12,None,None,23,24,None,25] 
    res=[[2],[4,8],[5,19,10],[13,12,23,24,25]]
    assert Solution().levelOrder(build_tree(tree)) == res

    assert Solution().levelOrder(build_tree([]))==[]
    assert Solution().levelOrder(build_tree([4]))==[[4]]

    built_tree = build_tree([3,9,20,None,None,15,7])
    assert Solution().levelOrder(built_tree) == [[3],[9,20],[15,7]]

main()
# tree=[2,4,8,5,null,9,0,3,2,3,4,null,5]       