# /*
#  * Input: (length=7)
#  *     [
#  *       { id: '1' },
#  *       { id: '2', parent: { id: '1' } },
#  *       { id: '3' },
#  *       { id: '4', parent: { id: '3' } },
#  *       { id: '5', parent: { id: '3' } },
#  *       { id: '6', parent: { id: '5' } },
#  *       { id: '7', parent: { id: '5' } }
#  *     ]

class Node:
    def __init__(self, val, parent_idx=None):
        self.val = val
        self.parent_idx = parent_idx
        self.children = []
        self.visited = False
        
nodes = (None, Node(1), Node(2,1), Node(3,1), Node(4,3), Node(5,3), Node(6),
        Node(7), Node(8), Node(9, 8))

def get_children(nodes):
    for i in range(1, len(nodes)):
        v = nodes[i]
        if v.parent_idx:
            nodes[v.parent_idx].children += [v]
            
get_children(nodes)
assert nodes[1].children == [nodes[2], nodes[3]]
assert nodes[3].children == [nodes[4], nodes[5]]
assert not nodes[6].children and not nodes[4].children

def dfs(v):
    v.visited = True
    v_descs = []
    for w in v.children:
        v_descs += [dfs(w)]
    return (v.val, v_descs)
assert dfs(nodes[3]) == (3, [(4,[]), (5,[])])

rootlist = []
for i in range(1, len(nodes)):
    v = nodes[i]
    if not v.visited and not v.parent_idx:
        rootlist += [dfs(v)]

assert rootlist == [
    (1, [(2, []), (3, [(4, []), (5, [])])]), 
    (6, []), 
    (7, []), 
    (8, [(9, [])]),
]

rootlist = [
    (10, []),
    (8, [(9, [])]),
    (1, [(2, []), (3, [(4, []), (5, [])])]), 
    (6, []), 
    (7, []), 
]
from typing import List
def clean_rootlist(rootlist):
    def dfs_helper(sublist:List):
        assert type(sublist) is list
        for lnidx, listnode in enumerate(sublist):
            if listnode[1] == []:
                sublist[lnidx] = listnode[0]
            else:
                dfs_helper(listnode[1])

    dfs_helper(rootlist)

clean_rootlist(rootlist)
assert rootlist == [10, (8, [9]), (1, [2, (3, [4,5])]), 6, 7]


# clas			
#  * Output: (length=2)
#  *     [
#  *       {
#  *         id: '1',
#  *         children: [
#  *           {
#  *             id: '2'
#  *           }
#  *         ]
#  *       },
#  *       {
#  *         id: '3',
#  *         children: [
#  *           {
#  *             id: '4'
#  *           }, 
#  *           {
#  *             id: '5',
#  *             children: [
#  *               {
#  *                 id: '6'
#  *               },
#  *               {
#  *                 id: '7'
#  *               }
#  *             ]
#  *           }
#  *         ]
#  *       }
#  *     ]
#  */