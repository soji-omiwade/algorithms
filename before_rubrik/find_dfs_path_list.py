class Node:
    def __init__(self, key, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right
    
def find_path(x: Node, key):
    """complexity
    time: T(n) = O(1) + 2 T(n/2) --> T(n) = O(1)
    space: O(n), since 
        1) the recursion stack could be O(n) in size
        2) the path lists each can be O(n)
    """
    if not x:
        return None
    if x.key == key:
        return [x.key]
    a = find_path(x.left, key)
    if a:
        return a + [x.key]
    a = find_path(x.right, key)
    if a:
        return a + [x.key]
    return []
    
root = Node(1,
            Node(2, 
                Node(4, 
                    Node(8),
                    Node(9)),
                Node(5,
                    Node(10))),
            Node(3, Node(6), Node(7)))
            
assert root.left.key == 2
assert root.left.left.key == 4
assert root.right.left.key == 6
assert not root.right.left.right 
assert find_path(root, 6) == [6, 3, 1]
assert find_path(root, 1) == [1]
assert find_path(root, 42) == []
assert find_path(root, 9) == [9, 4, 2, 1]
assert find_path(None, 42) is None