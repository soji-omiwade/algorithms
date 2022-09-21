from typing import List, Dict, Tuple
from pprint import pprint
import random

class Node:
    def __init__(self, val):
        self.val = val
        self.nbs = []
        
    def __str__(self):
        return super().__str__() + f'\t{self.val}: {[v.val for v in self.nbs]}'
        
def get_nodes_from_graph_rep(graph_rep: List[List[int]]):
    nodes = {}
    for v_and_nbs in graph_rep:
        it = iter(v_and_nbs)
        idx = next(it)
        if idx not in nodes:
            nodes[idx] = Node(idx)
        v = nodes[idx]
        for nb_idx in it:
            if nb_idx not in nodes:
                nodes[nb_idx] = Node(nb_idx)
            nodes[idx].nbs += [nodes[nb_idx]]
            nodes[nb_idx].nbs += [nodes[idx]]
    return nodes

def bfs_history(nodes: Dict[int, Node], start) -> Dict[int, Node]:
    from collections import deque
    history = {v:None for v in nodes.values()}
    count = 0
    q = deque()
    q += [nodes[start]]
    while len(q) > 0:
        v = q.popleft()
        count += 1
        history[v] = count
        for w in sorted(v.nbs, key=lambda v:v.val):
            if history[w] is None:
                q.append(w)
                history[w] = 0
    return history
    
graph_rep = [
    [1,2,5,3],
    [8,9,10],
    [11],
    [2,4,5,3],
    [4,5],
    [3,6,7],
]
random.shuffle(graph_rep)
nodes = get_nodes_from_graph_rep(graph_rep)
history = bfs_history(nodes, start=1)
try: 
    assert [(v.val, history[v]) for v in sorted(history, key=lambda v:v.val) if history[v] is not None] == [
        (1,1),
        (2,2),
        (3,3),
        (4,5),
        (5,4),
        (6,6),
        (7,7),
    ]
except Exception as e:
    pprint([(v.val, history[v]) for v in sorted(history, key=lambda v:v.val) if history[v] is not None])
    raise e