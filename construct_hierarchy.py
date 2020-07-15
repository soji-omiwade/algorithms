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

assert rootlist = [
    (1, [(2, []), (3, [(4, []), (5, [])])]), 
    (6, []), (7, []), 
    (8, [(9, [])]),
]

rootlist = [
    (10, []),
    (8, [(9, [])]),
    (1, [(2, []), (3, [(4, []), (5, [])])]), 
    (6, []), (7, []), 
]
from typing import List
def clean_rootlist(rootlist):
    def clean_helper(descs:List):
        for listnode in descs:
            ...
            clean_helper(idx, *item)
                
    for listnode in rootlist:
        if listnode[1] == []:
            listnode = listnode[0]
        else:
            clean_helper(listnode[1])
        
    rootlist[i] = clean_helper(item[1])
clean_rootlist(rootlist)

assert rootlist == [(1, [2, (3, [4,5])]), 6, 7, 8]
# def construct_hierarchy(g: List[Node]) -> List[Node]:
    # """
    # assert (
        # g[2].parent == 1 and g[4] == 3 and
        # g[5] == 3
    # )
    # """
    # output_nodes = {}
    
    
    # try:
        # output_nodes[2]
    # except KeyError:
        # pass
    # else:
        # raise Exception("should have bombed")
    # return output_nodes

# first output:
	# (1, [(2)])
	# (2, [])
	# (3, [(4), (5)])
	# (4, [])
	# (5, [(6),(7)])
	# (6, [])
	# (7, [])
# second output: 
	# (1, [(2)])
	# (2, [])
	# (3, [(4), (5, [(6),(7)])])
	# (4, [])
	# (6, [])
	# (7, [])
	
# assert output[n1] == [n2]
# assertKeyError     
# for node in nodes: 
		# gather_nodes()
		
# def gather_nodes(node, res:
		# if node.visit:
			# return
		# node.visit = True
		# res += [node]
	
	# for each child of node: 
		# print_node(child.key)

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