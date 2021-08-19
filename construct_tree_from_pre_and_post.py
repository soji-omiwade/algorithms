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
    9
2
pre: 5 9 2
post 2 9 5

interesting...

won't look at the answer yet. I will keep digging. i may yet get this
pre:  5 8 7 3 9 2
post: 7 3 8 2 9 5
      0 1 2 3 4 5


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
    
    
root = construct_tree_from_pre_and_post(pre, post)
preorder(root) # testing framework: should match pre above
