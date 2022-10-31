from treenode import TreeNode
from typing import List
def buildtree(tl: List[int]) -> TreeNode:
    if not tl:
        return None
    d={}
    root=TreeNode(tl[0])
    d[0]=root
    for i in range(len(tl)):
        if tl[i] and 2*i+1<len(tl):
            v=d[i]
            v.left=None
            if tl[2*i+1] is not None:
                v.left=TreeNode(tl[2*i+1])
            v.right=None
            if tl[2*i+2] is not None:
                v.right=TreeNode(tl[2*i+2])
            d[2*i+1]=v.left
            d[2*i+2]=v.right
    return root

def get_node(v,val)->TreeNode:
    if v.val == val:
        return v
    if v.left:
        w = get_node(v.left,val)
        if w:
            return w
    if v.right:
        return get_node(v.right, val)
