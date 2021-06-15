'''
pre =  [1,2,4,5,3,6,7]
post = [4,5,2,6,7,3,1]
       [0,1,2,3,4,5,6]
Output: [1,2,3,4,5,6,7]

'''
    
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from itertools import chain
class Solution:
    def constructFromPrePost(self, pre: List[int], post: List[int]) -> TreeNode:
        #pre = [1,2,4,5,3,6,7]
        #post = [4,5,2,6,7,3,1]
        def traverse(prestart: int, preend: int, poststart: int, postend: int) -> TreeNode: # 0, 6, 0, 6, [1,3,0,2], [2,2,0,0]
            if prestart > preend:
                return None
            root = TreeNode(pre[prestart]) # n1, n2, n4
            if prestart == preend:
                return root
            leftpreend = preidx[post[postend - 1]] - 1 # 4 - 1 = 3.... 3 - 1 = 2.......
            leftpostend = postidx[pre[prestart + 1]]   # 2.....0
            root.left = traverse(prestart + 1, leftpreend, poststart, leftpostend)  # 1, 3, 0, 2.....[2,2,0,0]
            root.right = traverse(leftpreend + 1, preend, leftpostend + 1, postend - 1) # 4, 6, 3, 5.....[3,3,1,1]
            return root
        # preidx[0] = None
        # preidx[3] = 5
        # preidx[2] = 1
        preidx = [None] * (1 + len(pre))
        postidx = [None] * (1 + len(pre))
        for idx, (preval, postval) in enumerate(zip(pre, post)):
            postidx[postval] = preidx[preval] = idx
        return traverse(0, len(pre) - 1, 0, len(pre) - 1)