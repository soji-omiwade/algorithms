edges=[]
with open("greedy_shortest_path_with_dfs.in") as f:
    s=f.readline()
    src,dst = s.split()
    for line in f:
        a,b,c=line.split()
        edges.append((a,b,float(c)))
print(src,dst)
print(edges)

def build_graph(edges):
    class Node:
        a=42
        def __init__(self, key):
            self.key=key
            self.nbs=set([])
    nodes={}
    for e in edges:
        k,kp,_=e
        try:
            u = nodes[k]
        except:
            u = Node(k)
            nodes[k]=u
        try:
            v = nodes[kp]
        except:
            v = Node(kp)
            nodes[kp]=v
        u.nbs.add(v)
        v.nbs.add(u)
    return nodes
        
G = build_graph(edges)

from collections import deque
q = deque([G[src]])
visited = {G[u]:False for u in G}
pi={G[u]:None for u in G}
cost=0
while q:
    v = q.popleft()
    cost+=1
    if v.key == dst:
        break
    visited[v] = True
    for u in v.nbs:
        if not visited[u]:
            pi[u]=v
            q.append(u)

print(cost)
for v in pi:
    try:
        pi_v_key=pi[v].key
    except:
        pi_v_key=None
    print((v.key,pi_v_key), end="-")
print()
path=[]
v=G[dst]
while True:
    path.append(v.key)
    v = pi[v]
    if not v:
        break
while path:
    print(f"{path.pop()}",end=",")
print()
