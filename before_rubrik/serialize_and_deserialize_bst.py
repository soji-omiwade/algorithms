'''
time: 10:18
sit tight
relax
have fun

serialize BFS (2)
    * construct tree from in and pre
    * construct_in
    * construct_pre
    testing
        * same tree 

pseudocode
    serialize
        construct in and pre lists
        save as str -> in + '*' * 'pre'
    deserialize (data)
        in, pre = split via *
        convert them to lists (simple cast)
        call construct_tree_from_in_and_pre
'''

# Definition for a binary tree node.
from typing import List

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """
        def construct_in(node, res):
            if not node:
                return
            construct_in(node.left, res)
            inlistloc_lookup[node] = len(res)
            res.append(node.val)
            construct_in(node.right, res)
            
        def construct_pre(node, res):
            if not node:
                return
            res.append((node.val, inlistloc_lookup[node]))
            construct_pre(node.left, res)
            construct_pre(node.right, res)
        
        intree_aslist = []
        pretree_aslist = []
        inlistloc_lookup = {}
        construct_in(root, intree_aslist)
        construct_pre(root, pretree_aslist)
        return str(intree_aslist) + "*" + str(pretree_aslist)
        
        

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        
        loclookup[i think]
        get the next from pre, and split in accordingly
        [(5,1) 6 10 11] * [(5,1) 10 6 11]
        """
        def populate_lookup():
            ...
            
        '''
        pre [(5,2),(3,0),(5,1),(6,4),(5,3),(11,5)]
        in  [3 5 5 5 6 11] 
        '''
        def construct_tree_from_in_and_pre(lo: int, hi: int) -> TreeNode:
            nonlocal preidx
            if lo > hi:
                return None
            rootval, rootloc  = prelist[preidx]
            preidx += 1
            root = TreeNode(rootval)
            root.left = construct_tree_from_in_and_pre(lo, rootloc - 1)
            root.right = construct_tree_from_in_and_pre(rootloc + 1, hi)
            return root
        splitdata = data.split('*')
        inlist, prelist = eval(splitdata[0]), eval(splitdata[1])
        preidx = 0
        tree = construct_tree_from_in_and_pre(0, len(prelist) - 1)
        return tree

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
ser = Codec()
deser = Codec()
root = TreeNode(5)
three =  TreeNode(3)
six = TreeNode(6)
root.left, root.right = three, six
three.right = TreeNode(5)
six.left = TreeNode(5)
six.right = TreeNode(11)

'''
what i will do:
    preorder: "hey in what's the inlist loc for this TreeNode" .... five!
    prelist.append((5,loc-of-this-5-node))
    so i need
        lookup[TreeNode] -> inlistloc
        ...

     5
 3       6
   5   5    11
'''
tree_string = ser.serialize(root)
print(tree_string) #in [3 5 5 5 6 11] * [(5,2),(3,0),(5,1),(6,4),(5,3),(11,5)]
ans = deser.deserialize(tree_string)

print(ans.val)
print(ans.left.right.val)

def same_tree(t1, t2):
    #both null!
    if t1 is t2 is None:
        return True
        
    #one null!!
    if (not t1 and t2) or (t1 and not t2):
        return False
        
    #none null!!!
    if t1.val != t2.val:
        return False
    return same_tree(t1.left, t2.left) and same_tree(t1.right, t2.right)

assert same_tree(ans, root)