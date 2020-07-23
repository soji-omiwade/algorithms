import random
from typing import List, Tuple, Dict

class Node:
    def __init__(self, val):
        self.val = val
        self.nbs = []
    def __str__(self):
        return f'{str(self.val)} {sorted(v.val for v in self.nbs)}'
        
def get_nodes_from_graph_rep(graph_rep):
    nodes = {}
    for point in graph_rep:
        it = iter(point)
        idx = next(it)
        if idx not in nodes:
            nodes[idx] = Node(idx)
        for nb_idx in it:
            if nb_idx not in nodes:
                nodes[nb_idx] = Node(nb_idx)
            nodes[idx].nbs += [nodes[nb_idx]]
            nodes[nb_idx].nbs += [nodes[idx]]
    return nodes
    
def lfs(nodes: Dict[int, Node], start_idx) -> List[List[int]]:
    from collections import deque
    q = deque([nodes[start_idx]])
    count = len(q)
    res = []
    visit = set([nodes[start_idx]])
    while len(q) > 0:
        res += [[]]
        for i in range(count):
            v = q.popleft()
            res[-1] += [v.val]
            for w in v.nbs:
                if w not in visit:
                    q += [w]
                    visit |= {w}
        res[-1].sort()
        count = len(q)
    return res

graph_rep = [
    [1,2,5,3],
    [8,9,10],
    [11],
    [2,4,5,3],
    [4,5],
    [3,6,7],
]

try:
    nodes = get_nodes_from_graph_rep(graph_rep)
    assert str(nodes[1]) == '1 [2, 3, 5]'
    assert str(nodes[3]) == '3 [1, 2, 6, 7]'
except AssertionError as ae:
    print(nodes[1])
    print(nodes[3])
    raise ae
    
nodes = get_nodes_from_graph_rep(graph_rep)
ll = lfs(nodes, 1)
try:
    assert ll == [
        [1], [2,3,5], [4,6,7]
    ]
except:
    print(ll)
    raise 