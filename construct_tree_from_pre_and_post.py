class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
'''
construct tree from pre and post order traversal
            5
        8       9
      7   3        2
      
5
    9
        2
pre: 5 9 2
post 2 9 5



      5
     /
    8
pre: 5 8
       ^
post: 8 5
      ^

        5
    9
2
pre: 5 9 2
post 2 9 5

interesting...

won't look at the answer yet. I will keep digging. i may yet get this
pre:  5 8 7 3 9 2
            ^
post: 7 3 8 2 9 5
          ^
      0 1 2 3 4 5

            5
         /     \
        8
       /
      7
      
      
function main(pre, post) -> treenode
    return construct(0)[1]
    
function treenode construct(preidx) # 2
        root = TreeNode(pre[preidx])
        if there are unvisited nodes to the left of node[preidx] 
            preidx, root.left = construct(preidx + 1)  #2
        if ...
            preidx, root.right = construct(preidx + 1)
        return preidx, root
'''   
def construct_tree_from_pre_and_post(pre, post):
    def helper(pre, post):
        nonlocal preidx, postidx
        root = TreeNode(pre[preidx])
        preidx += 1
        if root.val != post[postidx]:
            root.left = helper(pre, post)
        if root.val != post[postidx]:
            root.right = helper(pre, post)
        postidx += 1
        return root 

    preidx = postidx = 0
    return helper(pre, post)

def preorder(root):
    if not root:
        return
    preorder(root.left)
    preorder(root.right)
    print(root.val)


pre =[5, 8, 7, 3, 9, 2]
post= [7, 3, 8, 2, 9, 5]
    
root = construct_tree_from_pre_and_post(pre, post)
preorder(root) # testing framework: should match pre above
