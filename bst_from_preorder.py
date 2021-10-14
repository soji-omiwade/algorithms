# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
problem
example
    preorder = [8,5,1,7,10,12]
    inorder = [1, 5, 7, 8, 10, 12] #sorted of preorder
    output = tree rooted at 8


approach
    n = len(preorder)
    build lookup
    return helper()
    
    function helper(lo=0, hi=n)
        if lo > hi
            return None
        rootidx = lookup[preorder[0]] #lookup[8] = 3
        root = Node(inorder[rootidx])
        root.left = helper(lo, rootidx - 1)
        root.right = helper(rootidx + 1, hi)
        return root
        
    time: O(n lg n     + n ) -- sorted + traverse each element of preorder in tree construction in O(1)
    space: O(h) -- height of tree
    
tradeoffs
can also use bisect left

copy
    preorder = [8,5,1,7,10,12]
    inorder = [1, 5, 7, 8, 10, 12] #sorted of preorder
'''
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        def buildlookup():
            lookup = {}
            inorder = sorted(preorder)
            for idx, val in enumerate(inorder):
                lookup[val] = idx
            return lookup
        
        def helper(inorderlo, inorderhi, preidx): #4, 5
            if inorderlo > inorderhi:
                return preidx - 1, None
            root = TreeNode(preorder[preidx])
            rootidx = bisect.bisect_left(inorder, preorder[preidx])
            preidx, root.left = helper(inorderlo, rootidx - 1, preidx + 1)
            preidx, root.right = helper(rootidx + 1, inorderhi, preidx + 1)
            return preidx, root

        inorder = sorted(preorder)
        return helper(0, len(preorder) - 1, 0)[1]

        
        