def say_hello():
    print('Hello, World')

for i in range(5):
    say_hello()


# 
# Your previous Plain Text content is preserved below:
# 
# We are constructing a shared file system.
# A given user will have access to the file system through one root node. 
# 
# (You can imagine a typical use case being a cloud-based storage provider. Users work out of their private folders and shared folders live inside).
# 
# We will enforce the constraint that every file/directory (node) has exactly one path to it to minimize confusion. (or put another way, from any node A to another node B in a directed graph G, there is at most one path along children from A to B).
# 
# Example data structure
# 
#     class Node:
#         id = 0  # type: int # unique node id
#         name = "" # type: str   # relative name
#         parents # type: List[Node]   # parents of node
#         children # type: List[Node]  # children of node
#         file_data # type: bytes  # content of node (if file)
# 
# 
# Implement the bind_parent() function, which adds a parent to a child node (altering nodes) and must enforce system constraints.
# 
# 
#     def bind(parent, child):  # type(Node, Node) -> 

def bind(u, v):  # type(Node, Node)
    if u in v.parents:
        raise AlreadyBoundException("already bound")
    u.children.append(v)
    v.parents.append(u)
    return None 

try: 
    bind(a, b) # if b is already a child of a, then do nothing
except AlreadyBoundException:
    
bind(a, b) # 


# Find all roots from u --> u/roots (walking parents)
# find all roots from v --> v/roots (walking parents)
# No child of u/roots can be a child of v/roots  (search!)

foo = find_roots(C, [])

def find_roots(v, res=None)->List[Node]:
    if res is None:
        res = []
    if v.parents == []:
        res.append(v)    
    for u in v.parents:
        find_roots(u, res)
    return res
bar = find_roots(C)

