import collections
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:
    def serialize(self, root):
        vals = []

        def preOrder(node):
            if node:
                vals.append(node.val)
                preOrder(node.left)
                preOrder(node.right)

        preOrder(root)

        return ' '.join(map(str, vals))

    # O( N ) since each val run build once
    def deserialize(self, data):
        vals = collections.deque(int(val) for val in data.split())

        def build(minVal, maxVal):
            if vals and minVal < vals[0] < maxVal:
                val = vals.popleft()
                node = TreeNode(val)
                node.left = build(minVal, val)
                node.right = build(val, maxVal)
                return node

        return build(float('-infinity'), float('infinity'))
        

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