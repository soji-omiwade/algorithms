# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        def helper(curr, path):
            if not curr:
               return
            path.append(str(curr.val))
            helper(curr.left, path)
            helper(curr.right, path)
            if curr.left is curr.right is None:
                paths.append("->".join(path))
            path.pop()
            
        paths = []
        helper(root, [])
        return paths
        