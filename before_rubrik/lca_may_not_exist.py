'''
root:
if pkey and qkey: return true otherwise return false

    5
   / \
  1   3
 /
0
find lca (assume first both keys: if both exist, we will have the lca)

function  TreeNode -> TreeNode, bool, bool
    if curr is nil
      return nil, false, false
      
    left_has, left_pfound, left_qfound = function (curr's left)
    right_has, right_pfound, right_qfound = function (curr'r right)
    if left_has and right_has
        return curr, true, true

    i_have = None
    if curr.val is p or q val:
        i_have = curr  
    if (left_has or right_has) and i_have:
        return i_have, true, true
    curr_pfound = curr.val == p.val
    curr_qfound = curr.val == q.val
    return (left_has or right_has or i_have, curr_pfound or left_pfound or right_pfound, curr_qfound or left_qfound or right_qfound)


main
    lca, pfound, qfound = function()
    if pfound and qfound:
        return lca
    return None

    


'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def function(curr: TreeNode) -> Tuple[TreeNode, bool, bool]:
            if not curr:
              return None, False, False

            left_has, left_pfound, left_qfound = function(curr.left)
            right_has, right_pfound, right_qfound = function(curr.right)
            if left_has and right_has:
                return curr, True, True
            i_have = curr.val in (p.val, q.val)
            if (left_has or right_has) and i_have:
                return curr, True, True
            curr_pfound = curr.val == p.val
            curr_qfound = curr.val == q.val
            return (left_has or right_has or i_have, curr_pfound or left_pfound or right_pfound, curr_qfound or left_qfound or right_qfound)

        lca, pfound, qfound = function(root)
        if pfound and qfound:
            return lca
        return None