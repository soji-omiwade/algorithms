# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
start: 9:38
end:  10:10
total: 32mins

time: O(n)
space: O(n) for set. O(h) if we use inorder traversal of the tree
inorder(curr)
rorder(curr)

function Treenode inorder(curr, st)
    while True
        if curr
            push curr on st
            curr = curr.left
        else
            ret = st.pop
            curr = ret.right
            return ret, curr
            
function Treenode rorder(curr, st)
    while True
        if curr
            push curr on st
            curr = curr.right
        else
            ret = st.pop
            curr = ret.left
            return ret, curr

icurr = root
rcurr = root
left, icurr = inorder(icurr, inorder_st)
right, rcurr = rorder(rcurr, rorder_st)
inorder_st = []
rorder_st = []
while left is not right:
    if left.val + right.val == k:
        return True
    if left.val + right.val < k:
        left, icurr = inorder(icurr, inorder_st)
    else:
        right, rcurr = rorder(rcurr, rorder_st)
return False

3....6 k = 9
inorder()

constraints:
are vals unique? => nodes
'''
class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        def inorder(curr, st) -> Tuple[TreeNode, TreeNode]:
            while True:
                if curr:
                    st.append(curr)
                    curr = curr.left
                else:
                    ret = st.pop()
                    curr = ret.right
                    return ret, curr

        def rorder(curr, st) -> Tuple[TreeNode, TreeNode]:
            while True:
                if curr:
                    st.append(curr)
                    curr = curr.right
                else:
                    ret = st.pop()
                    curr = ret.left
                    return ret, curr

        icurr = root
        rcurr = root
        inorder_st = []
        rorder_st = []
        left, icurr = inorder(icurr, inorder_st)
        right, rcurr = rorder(rcurr, rorder_st)
        while left is not right:
            if left.val + right.val == k:
                return True
            if left.val + right.val < k:
                left, icurr = inorder(icurr, inorder_st)
            else:
                right, rcurr = rorder(rcurr, rorder_st)
        return False
        