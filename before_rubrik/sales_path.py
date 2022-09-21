from collections import deque
def get_cheapest_cost(rootNode): 
  nodes = deque([rootNode])
  mincost = float("inf")
  nodecost = {rootNode:0}
  while nodes:
    node = nodes.popleft()
    if not node.children:
      mincost = min(mincost, nodecost[node])
    else:
      for child in node.children:
        nodes.append(child)
        nodecost[child] = child.cost + nodecost[node]
  return mincost

class Node:
  def __init__(self, cost):
    self.cost = cost
    self.children = []
    self.parent = None


n0, n5, n3, n6, n2, n00, n1, n55 = Node(0), Node(5), Node(3), Node(6), Node(2), Node(3), Node(1), Node(5)
n0.children = [n5, n3, n6]
n3.children = [n2, n00]
n6.children = [n1, n5]

print(get_cheapest_cost(n0))