from find_dfs_path_list import find_path
class Node:
    def __init__(self, key, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right
def lca(root, x, y):
    px = find_path(root, x)
    py = find_path(root, y)
    m, n = len(px), len(py)
    
    #while loop
    i = 0
    while i < min(m, n) and px[m-1-i] == py[n-1-i]:
        i += 1
    #end while loop
    
    #for range
    # if n > m:
        # px, py = py, px
    # for i in range(m):
        # if px[m-1-i] != py[n-1-i]:
            # break
    # else:
        # i = 1
    # end for range
    return px[m-i]

root = Node(1, 
        Node(2, Node(4, Node(8), Node(9)), Node(5, Node(10))), 
        Node(3, Node(6), Node(7)))
assert root.left.key == 2
assert root.left.left.key == 4
assert root.right.left.key == 6

print(lca(root, 8, 10))
assert lca(root, 8, 10) == 2
assert lca(root, 6, 8) == 1
assert lca(root, 2, 5) == 1