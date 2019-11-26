"""
0 3
0 1 100
0 2 500
2 3 50
"""

"""1 2 200"""
import sys
from collections import defaultdict
class Node:
    def __init__(self, key):
        self.key = key
        self.adj = []

def dfs(v, s, t, nodes,*,visited=defaultdict(bool), cost):
    val=0
    if v is t: return 0,True
    
    for w in v.adj:
        if not visited[w]:
            visited[w]=True
            ds_cost, done = dfs(w,s,t,nodes,visited=visited,cost=cost)
            print(f"visit: {(v.key,w.key)}")
            if done: return cost[(v,w)]+ds_cost, done
    return None,False

def main():
    nodes={}
    cost={}
    with open(sys.argv[1]) as f:
        src, dst = f.readline().split()
        src, dst = int(src), int(dst)
        for line in f:
            uk,vk,cst = line.split()
            uk,vk,cst = int(uk),int(vk),float(cst)
            if uk not in nodes:
                nodes[uk] = Node(uk)
            if vk not in nodes:
                nodes[vk] = Node(vk)
            nodes[uk].adj.append(nodes[vk])
            cost[(nodes[uk],nodes[vk])]=cst
    print(dfs(nodes[src],nodes[src],nodes[dst],nodes,cost=cost)[0])
        
if __name__=="__main__":
    main()