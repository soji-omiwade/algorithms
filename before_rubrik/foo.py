# This code is contributed by Divyanshu Mehta 
#geeksforgeeks
from collections import defaultdict

class Graph:
    def __init__(self):
        self.V = V
        self.graph = defaultdict(list)
    
    def add_edge(self,src,dest,weight):
        self.graph[src].append((weight,dest))
        self.graph[dest].append((weight,src))
        
    def dijkstra(self,u):
        V=self.V
        dist=[]
        
        min_heap=Heap()
        
        for v in range(V):
            dist.append(sys.maxsize)
            min_heap.array.append(min_heap.new_min_heap_node(v,dist[v]))
            min_heap.pos.append(v)
    
        
if __name__=="__main__":
    graph = Graph(6)
    graph.add_edge(0,1,4)
    graph.add_edge(0,7,8)
    graph.add_edge(1,2,8)
    graph.add_edge(1,7,11)
    graph.add_edge(2,8,2)
    graph.add_edge(7,8,7)
    
    graph.add_edge(2,42,10)
    graph.add_edge(8,42,0)
    
graph.dijkstra(0)
