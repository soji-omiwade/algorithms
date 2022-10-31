'''
first of find all the deepest leaves
iteratively find their LCAa
    find all the paths from root to deepes leaves
    go down with  a slider until u find a non-common node. then return the prev non-common
    
t: O(n + nlgn + n lg n) = 


at node 
    get_maxdepthleft
    getmaxdepth right
    if dleft == dright
        then i am the LCA
    else
        recurse down to the node with bigger maxdepth
        
function helper(curr)
    if curr is a leaf
         1, curr
    leftscore, leftres = helper(left)
    rightscore, rightres = helper(right)
    if leftscore == rightscore
        return 1 + maxscore,curr
    else
        1 + maxscore, the node with higher score
        
constraints
---
root
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: TreeNode) -> TreeNode:
        def helper(curr):
            if not curr:
                return 0, None
            leftscore, leftres = helper(curr.left)
            rightscore, rightres = helper(curr.right)
            if leftscore == rightscore:
                return 1 + leftscore, curr
            if leftscore > rightscore:
                return 1 + leftscore, leftres
            return 1 + rightscore, rightres
                    
        if not root:
            return None
        return helper(root)[1]
        