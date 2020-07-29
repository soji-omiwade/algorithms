from typing import Dict, List, Tuple, Union

class Node:
    def __init__(self, val, children=None):
        self.val = val
        self.children = children
        if not self.children:
            self.children = []
            
def construct_hierarchy(parent: Dict[Node, Node], nodes: List[Node]) -> List[Tuple]:
    def helper(v: Node) -> Tuple[int, List[Tuple]]:
        'example return: (3, [(4,[])])'
        res = (v.val, [])
        for w in v.children:
            res[-1].append(helper(w))
        res[-1].sort()
        return res
    res = []
    for v in nodes:
        if v not in parent:
            res.append(helper(v))
    return sorted(res)

def set_children(*nodes, **kwds):
    parent = kwds['parent']
    for w, v in parent.items():
        v.children.append(w)

nodes = []
for i in range(1,13):
    exec(f'n{i} = Node({i}); nodes.append(n{i})')

parent = {}
parent[n2] = parent[n3] = n1
parent[n4] = parent[n5] = n6
parent[n8] = parent[n9] = n4
parent[n10] = parent[n11] = parent[n12] = n9
set_children(nodes,parent=parent)

print(construct_hierarchy(parent, nodes))
# assert construct_hierarchy(parent, nodes) == [(1,[(2,[]),(3,[])]), (6,[(4,[]),(5,[])]), (7,[])]
assert construct_hierarchy(parent, nodes) == [(1,[(2,[]),(3,[])]), (6,[(4,[(8,[]),(9,[(10,[]),(11,[]),(12,[])])]),(5,[])]), (7,[])]

def pprint_hierarchy(hierarchy: List[Tuple]) -> List[Union[int, Tuple]]:
    for i, (vval, vdescs) in enumerate(hierarchy):
        if vdescs == []:
            hierarchy[i] = vval
        else:
            pprint_hierarchy(vdescs)
    return hierarchy

def pprint_hierarchy_copy(hierarchy: List[Tuple]) -> List[int or Tuple]:
    res = []
    for i, (vval, vdescs) in enumerate(hierarchy):
        if vdescs == []:
            res.append(vval)
        else:
            res.append((vval,pprint_hierarchy_copy(vdescs)))
    return res
    
if __name__ == '__main__':
    hierarchy = [(2,[]), (3,[]), (4,[])]
    assert pprint_hierarchy(hierarchy) == [2,3,4]
    
    hierarchy = [(2,[]), (4,[(3,[]),(5,[])])]
    assert pprint_hierarchy(hierarchy) == [2,(4,[3,5])]

    hierarchy = [(2,[]), (3,[]), (4,[])]
    assert pprint_hierarchy(hierarchy) == [2,3,4]    

    hierarchy = [(2,[]), (3,[]), (4,[])]
    res = pprint_hierarchy_copy(hierarchy)
    assert res is not hierarchy
    assert  res == [2,3,4]
    
    hierarchy = [(2,[]), (4,[(3,[]),(5,[])])]
    assert pprint_hierarchy_copy(hierarchy) == [2,(4,[3,5])]

    hierarchy = [(2,[]), (3,[]), (4,[])]
    assert pprint_hierarchy_copy(hierarchy) == [2,3,4]    
