'''
output:
               1
            /       \
           2         3
          / \       / \
         4   5     6   7
input: pre: [1,2,4,5,3,6,7] post: [4,5,2,6,7,3,1] 
             ^                     ^
root node is not constrained
so node will continue to recurisvely make nodes as long as what is on post is not node
we have to naturally progress down the tree (pre-progress)

preidx = postidx = 0 
construct(pre, post)
    root = makenode(preidx)
    preidx += 1
    if nodes to left of me in pre
        root.left = construct(pre, post)
    if still nodes to left of me 
        root.right = construct(pre, post)
    postidx += 1
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    preidx = postidx = 0 
    def constructFromPrePost(self, pre: List[int], post: List[int]) -> TreeNode:
            root = TreeNode(pre[preidx])
            preidx += 1
            if post[postidx] != root.val:
                root.left = self.constructFromPrePost(pre, post)
            if post[postidx] != root.val:
                root.right = self.constructFromPrePost(pre, post)
            postidx += 1
            return root