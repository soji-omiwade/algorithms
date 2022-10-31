class Node:
    def __init__(self, key, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right
    
def find(x: Node, key):
    if not x:
        return ""
    if x.key == key:
        return str(x.key)
    s = find(x.left, key)
    if s:
        return str(x.key) + s
    s = find(x.right, key)
    if s:
        return str(x.key) + s
    return ""
    
root = Node(1,
            Node(2, 
                Node(4, 
                    Node(8), 
                    Node(9)),
                Node(5, Node(10))), 
            Node(3, Node(6), Node(7)))
            
assert root.left.key == 2
assert root.left.left.key == 4
assert root.right.left.key == 6
assert not root.right.left.right 
assert find(root, 6) == "136"
assert find(root, 1) == "1"
assert find(root, 42) == ""
assert find(root, 9) == "1249"