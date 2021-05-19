# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        while True:
            if p.val < root.val > q.val:
                root = root.left
            elif p.val > root.val < q.val:
                root = root.right
            else:
                break
        return root
        
one = TreeNode(1)
three = TreeNode(3)
eight = TreeNode(8)
ten = TreeNode(10)
zero = TreeNode(0, None, one)
four = TreeNode(4, three, None)
seven = TreeNode(7, None, eight)
nine = TreeNode(9, None, ten)
two = TreeNode(2, zero, four)
eight = TreeNode(8, seven, nine)
five = TreeNode(5, two, eight)


lca = Solution().lowestCommonAncestor
assert lca(five, four, eight) is five
assert lca(five, three, one) is two
assert lca(five, ten, nine) is nine
 