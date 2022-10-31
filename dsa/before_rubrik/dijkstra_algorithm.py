from math import inf
from graph_priority_queue import GraphPriorityQueue

def build_graph(edges, *, directed = False):
    class Node:
        def __init__(self, key):
            self.key = key
            self.nbs = set([])
        def __str__(self):
            return str(self.key)
    g,w={},{}
    #foo: given something in input set, return back the integral index
    coo = []
    foo = {} 
    for iiu,iiv,c in edges:
        try: 
            iu = foo[iiu]
        except: 
            foo[iiu] = iu = len(foo)
            coo.append(iiu)
        try: 
            iv = foo[iiv]
        except:
            foo[iiv] = iv = len(foo)
            coo.append(iiv)
            
        try:
            u = g[iu]
        except:
            u = Node(iu)
        try:
            v = g[iv]
        except:
            v = Node(iv)
        u.nbs.add(v)
        g[iu],g[iv] = u,v
        w[u,v] = c
        if not directed:
            v.nbs.add(u)        
            w[v,u] = c
    return g,w,coo,foo

def initialize_single_source(g, s):
    d = {v:inf for v in g.values()}
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
        if d[u] == inf:
            path[u.key] = []
        elif u is not s:
            path[u.key] = path[pi[u].key] + [u.key] 
        for v in u.nbs:
            relax(u,v,w,d,pi,pq)            
    return path,d

def relax(u, v, w, d,pi,pq):
    if d[u] + w[u,v] < d[v]:
        d[v] = d[u] + w[u,v]
        pi[v] = u
        pq.decrease_key(v.key, d[v])

if __name__ == "__main__":
    edges = [("a","b",1), ("b","c",1), ("c","a",10), ("c","bb",1)]
    src = "bb"
    s,t,x,y,z = "stxyz"
    edges = [(s,t,10),(s,y,5), (t,x,1), (t,y,2), (y,t,3), (y,z,2), (y,x,9), (x,z,4), (z,s,7), (z,x,6)]
    src = s
    g, w, coo, foo = build_graph(edges, directed = True)
    path, d = single_source_shortest_path(g, w, foo[src])
    for iv, vpath in path.items():
        print(coo[iv], [coo[key] for key in vpath]) 
    for v,vdist in d.items():
        print(coo[v.key], vdist)