# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x, *, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def helper(v, x, px):
            px.append(v)
            if v is x:
                return
            if v.left:    
                helper(v.left, x, px)
            if px[-1] is not v:
                return
            if v.right:
                helper(v.right, x, px)
            if px[-1] is not v:
                return
            px.pop()
        pp = []
        pq = []
        helper(root, p, pp)
        helper(root, q, pq)
        for vp, vq in zip(pp, pq):
            if vp is not vq:
                break
            res = vp
        return res
        
left = TreeNode(42,right=TreeNode(''))
right = TreeNode(420)
root = TreeNode('root', left=left, right=right)
leftright = TreeNode('')
left.right = leftright
lowestCommonAncestor = Solution().lowestCommonAncestor
assert lowestCommonAncestor(root, left, right) is root
assert lowestCommonAncestor(root, leftright, right) is root
assert lowestCommonAncestor(root, leftright, left) is left