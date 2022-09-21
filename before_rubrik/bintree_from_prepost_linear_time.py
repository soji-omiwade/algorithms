'''
output: [1,2,3,4,5,6,7]

Input: 
pre and post:
pre: [1,2,4,5,3,6,7]
      ^          
post: [4,5,2,6,7,3,1]
                   ^
     1          0, 6
   /   \
  2             (1,3) n2, 
 /  \
 

output: [1,2,null]
input: pre: [1,2]    post:[2, 1]

build preidx_from_val and postidx_from_val
return traverse(0, len(pre) - 1)
def traverse(prestart, preend)   # 0, 1
    if prestart > preend:
        return None
    if prestart == preend:
        return TreeNode(pre[prestart])                      
        
        
    leftprestart = prestart + 1                             # 1
    rootval = pre[prestart]                                 # 1
    postend = postidx_from_val[rootval]                     # 1 
    rightprestart = preidx_from_val[post[postend - 1]]      # 1 
    leftpreend =  rightprestart - 1                         # 0 
    rightpreend = preend                                    # 1
    root.left = traverse(leftprestart, leftpreend)          # 1,0
    root.right = traverse(rightprestart, rightpreend)       # 1,1
    return root
    
    make imm. to right the left child
    
      1
    /   \
   2     3
  / \   / \
 4   5 6   7 
------





--------
repeatedly come back to root

root = maketree from pre[0]
pre_from_second = iter(pre)
next(pre_from_second)
for preidx, preval in enumerate(pre_from_second)
    traverse(root, preval)

traverse(curr, val)
if left is null
    curr.left = val
elif in postorder val comes before left.val:   postorderloc[val] < postorderloc[left.val]
    traverse(left)
elif right is null
    curr.right = Node(val)
else # 
    traverse(right)

T: O(n lg n)

---------
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, pre: List[int], post: List[int]) -> TreeNode:
        def traverse(prestart, preend):   # 0, 1
            if prestart > preend:
                return None
            if prestart == preend:
                return TreeNode(pre[prestart])                      
            leftprestart = prestart + 1                             # 1
            rootval = pre[prestart]                                 # 1
            postend = postidx_from_val[rootval]                     # 1 
            rightprestart = preidx_from_val[post[postend - 1]]      # 1 
            leftpreend =  rightprestart - 1                         # 0 
            rightpreend = preend                                    # 1
            root = TreeNode(rootval)
            root.left = traverse(leftprestart, leftpreend)          # 1,0
            root.right = traverse(rightprestart, rightpreend)       # 1,1
            return root        

        preidx_from_val = {val: idx for idx, val in enumerate(pre)}
        postidx_from_val = {val: idx for idx, val in enumerate(post)}
        return traverse(0, len(pre) - 1)