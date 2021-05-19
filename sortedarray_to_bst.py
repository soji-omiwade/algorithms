from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right
def isequal(tree1: TreeNode, tree2: TreeNode):
    if bool(tree1) ^ bool(tree2):
        return False
    if not tree1 and not tree2:
        return True
    return  (tree1.val == tree2.val
        and isequal(tree1.left, tree2.left) 
        and isequal(tree1.right, tree2.right))
    
tree1 = TreeNode(0, 
    TreeNode(-10, None, TreeNode(-3)),
    TreeNode(5, None, TreeNode(9))
    )
tree2 = TreeNode(0, 
    TreeNode(-10, None, TreeNode(-3)),
    TreeNode(5, None, TreeNode(9))
    )
assert isequal(tree1, tree2)

tree1 = TreeNode(0, 
    TreeNode(-10, None, TreeNode(-3)),
    TreeNode(5, None, TreeNode(7))
    )
tree2 = TreeNode(0, 
    TreeNode(-10, None, TreeNode(-3)),
    TreeNode(5, None, TreeNode(9))
    )
assert not isequal(tree1, tree2)

tree1 = TreeNode(0, 
    TreeNode(-10, None, TreeNode(-3)),
    TreeNode(5, None, TreeNode(9))
    )
tree2 = TreeNode(0, 
    TreeNode(-10, None, TreeNode(-3)),
    TreeNode(5, TreeNode(4), TreeNode(9))
    )
assert not isequal(tree1, tree2)

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        def helper(lo: int, hi: int) -> TreeNode:
            if lo > hi:
                return None
            mid = (lo + hi)//2
            curr = TreeNode(nums[mid])
            curr.left = helper(lo, mid - 1)
            curr.right = helper(mid + 1, hi)
            return curr
        return helper(0, len(nums)-1)
        
nums = [-10, -3, 0, 5, 9]
atree = TreeNode(0, 
    TreeNode(-10, None, TreeNode(-3)),
    TreeNode(5, None, TreeNode(9))
    )
etree = Solution().sortedArrayToBST(nums)
assert isequal(etree, atree)