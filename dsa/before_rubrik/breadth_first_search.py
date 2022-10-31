"""
essentially a BFS
input: 
1 3
[(1,2), (0,2), (1,0), (2,3)]
"""
def build_graph(edges):

    class Node:
        def __init__(self, key):
            self.key = key
            self.nbs = set([])
        def __str__(self):
            foo=str(self.key)
            coo = []
            for v in self.nbs:
                coo.append(v.key)
            return foo + ": " + str(coo)
            
            
    nodes = {}
    for edge in edges:
        iu, iv = edge[0], edge[1]
        try: 
            u = nodes[iu]
        except: 
            u = Node(iu)
            nodes[iu] = u
        try: 
            v = nodes[iv]
        except: 
            v = Node(iv)
            nodes[iv] = v
        u.nbs.add(v)
        v.nbs.add(u)
    return nodes
    
src, dst = 1,3
edges = [(1,2), (0,2), (1,0), (2,3)]
from collections import deque
q = deque()
nodes = build_graph(edges)
s, t = nodes[src], nodes[dst]
q.append(s)
visited = {v:False for v in nodes.values()}
degree = {v:None for v in nodes.values()}
pi = {v:None for v in nodes.values()}
visited[s] = True
degree[s] = 0
while q:
    v = q.popleft()
    if v != t:
        for w in v.nbs:
            if not visited[w]:
                visited[w] = True
                q.append(w)
                degree[w] = degree[v] + 1
                pi[w] = v
            

print("degree: ")
for v in nodes.values():
    print(f"{str(v):20}{degree[v]:2}")
print("pi")
for v in nodes.values():
    print(f"{v}\t:{pi[v]}")
