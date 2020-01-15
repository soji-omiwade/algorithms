def build_graph(edges):
    g={}
    for e in edges:
        iu,iv,c = *e
        try: u = g[iu]
        except: u = Node(iu)
        try: v = g[iv]
        except: v = Node(iv)
        g[iu],g[iv] = u,v
        w[u,v] = c
    return g,w
    
def print_paths(path):
    for np in paths.values():
        print(np)

def dfs(g, w, src):
    s = g[src]
    d = {v:math.inf for v in g.values()}; d[s] = 0
    pi = {v:None for v in g.values()}
    initialize_single_source(g, s)
    pq = PriorityQueue(g)
    S = set([])
    path = {v:None for v in g.values()}; path[s] = str(s.key)
    while pq:
        u = g[pq.extract_min()]
        if u is not s:
            path[u] = path[pi[u]] + "-" + str(u.key)
        if u is not t:
            S.add(u)
            for v in u.nbs:
                relax(u,v,w,d,pi)
                
    return path
    
def relax(u, v, w, d,pi,pq):
    if d[u] + w[u,v] < d[v]:
        d[v] = d[u] + w[u,v]
        pi[v] = u
        pq.decrease_key(v.key, d[v])
    
class PriorityQueue:
    def is_empty(self):
        return self.n == 0
    def decrease_key(self, i, key):
        self.heap.a[i] = key
        self.heap.heapify(i)
    def extract_min(self):
        key=self.heap.a[0]
        a[0]=a[n-1]
        self.heap.n-=1
        self.heap.heapify(0)
        return key
    
    class MinHeap:
