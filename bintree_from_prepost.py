# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, pre: List[int], post: List[int]) -> TreeNode:
        preidx = 1
        postidx = len(post) - 1 - 1
        root = TreeNode(pre[0])
        lastpre = lastpost = root
        added = set([root.val])
        preturn = True
        while len(added) != len(pre):
            if preturn:
                val = pre[preidx]
                preidx += 1
            else: 
                val = post[postidx]
                postidx -= 1
            preturn = not preturn
            if not preturn and val not in added:
                lastpost.right = TreeNode(val)
            elif preturn and val not in added:
                lastpre.left = 
            added.add(val)