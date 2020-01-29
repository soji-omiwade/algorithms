def bfs(src):
    from collections import deque
    from collections import defaultdict
    visited = defaultdict(bool)
    paths = {src:[]}
    pi = {}
    dist = {}
    q = deque()
    q.append(src)
    count = 0
    while q != []:
        v = q.popleft()
        dist[v] = count
        count += 1
        if v != src:
            paths[v] = paths[pi[v]] + [v.key]
        for u in v.nbs:
            if not visited[u]:
                visited[u] = True
                q.append(u)
                pi[u] = v
    return dist, paths

class Graph:
    class Node:
        count = 0
        def __init__(self):
            self.key = Graph.Node.count
            Graph.Node.count += 1
            self.nbs = set([])
            
        def add_nb(self, v):
            self.nbs.add(v)
            v.nbs.add(self)
     
    def __init__(self, edges):
        from collections import defaultdict
        self.nodes = defaultdict(self.Node)
        for (i,j) in edges:
            self.nodes[i].add_nb(self.nodes[j])
    
    def __iter__(self):
        self.index = 0
        return self
        
    def __next__(self):
        if self.index == len(self.nodes):
            raise StopIteration
        res = self.nodes[self.index]
        self.index += 1
        return res
        
if __name__ == "__main__":
    edges = [(1,2), (0,2), (1,0), (2,3)]
    g = Graph(edges)
    dist, paths = bfs(next(iter(g)))
    for v in g:
        print(v.key,"-->", paths[v])