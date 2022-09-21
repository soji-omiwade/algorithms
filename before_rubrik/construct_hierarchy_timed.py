from typing import List, Dict, Tuple
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        self.children = []
def construct_hierarchy(parents: Dict[int,Node]) -> List[Tuple[Node, List[Node]]]:
    def helper(v):
        descs = []
        subres = (v.val, descs)
        for w in v.children:
            descs += [helper(w)]
        return subres
    nodes = {}
    for v, pv in parents.items():
        nodes[v.val] = v
        if pv is not None:
            nodes[pv.val] = pv
            pv.children += [v]
    res = []
    for idx, v in nodes.items():
        if parents[v] is None:
            res += [helper(v)]
    return res
    
n4 = Node(4)
n2 = Node(2, left=n4)
n3 = Node(3)
n1 = Node(1, n2, n3)
n5 = Node(5)
parents = {}
parents[n2] = parents[n3] = n1
parents[n4] = n2
parents[n5] = None
parents[n1] = None
hier = construct_hierarchy(parents)
try:
    assert hier == [(1, [(2, [(4, [])]), (3, [])]), (5,[])]
except AssertionError as ae:
    print(hier)
    raise ae