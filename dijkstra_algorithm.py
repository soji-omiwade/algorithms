import math
from graph_priority_queue import GraphPriorityQueue

def build_graph(edges):
    class Node:
        def __init__(self, key):
            self.key = key
            self.nbs = set([])
        def __str__(self):
            return str(self.key)
    g,w={},{}
    for iu,iv,c in edges:
        try:
            u = g[iu]
        except:
            u = Node(iu)
        try:
            v = g[iv]
        except:
            v = Node(iv)
        u.nbs.add(v)
        v.nbs.add(u)
        g[iu],g[iv] = u,v
        w[u,v] = w[v,u] = c
    return g,w
    
def print_paths(path):
    print(path)

def initialize_single_source(g, s):
    d = {v:math.inf for v in g.values()}
    d[s] = 0
    pi = {v:None for v in g.values()}
    return d, pi
    
def single_source_shortest_path(g, w, src):
    s = g[src]
    d, pi = initialize_single_source(g, s)
    pq = GraphPriorityQueue(len(g), src)
    S = set([])
    path = {}
    path[src] = [src]
    while not pq.is_empty():
        u = g[pq.extract_min()]
        S.add(u)
        if u is not s:
            path[u.key] = path[pi[u].key] + [u.key] 
        for v in u.nbs:
            relax(u,v,w,d,pi,pq)            
    return path
    
def relax(u, v, w, d,pi,pq):
    if d[u] + w[u,v] < d[v]:
        d[v] = d[u] + w[u,v]
        pi[v] = u
        pq.decrease_key(v.key, d[v])

if __name__ == "__main__":
    edges = [(0,1,1), (1,2,1), (2,0,10), (2,3,1)]
    g, w = build_graph(edges)
    path = single_source_shortest_path(g, w, 3)
    print_paths(path)