from typing import List, Tuple
def construct_hierarchy(parents) -> List[Tuple[int, List]]:
    def get_children(parents):
        from collections import defaultdict
        children = defaultdict(list)
        for v,pv in parents.items():
            if pv:
                children[pv] += [v]
        return children
        
    def dfs_helper(v, children) -> Tuple:
        if v not in children:
            return v.val
        descs = []
        for w in children[v]:
            descs += [dfs_helper(w, children)]
        return (v.val, descs)
        
    res = []
    children = get_children(parents)
    
    for v in nodes:
        if v not in parents or not parents[v]:
            res += [dfs_helper(v, children)]
    return res

class Node:
    def __init__(self, val):
        self.val = val
n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)
n8 = Node(8)
n9 = Node(9)
nodes = (n1, n2, n3, n4, n5, n8, n9)
parents = {n1:n2, n3:n2, n4:n2, n2:n5}
res = [(5, [(2, [1, 3, 4])]), 8, 9] 
assert construct_hierarchy(parents) == res
assert construct_hierarchy(parents) == res
assert construct_hierarchy(parents) == res


