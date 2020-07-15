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
def construct_hierarchy(g: List[Node]) -> List[Node]:
    """
    assert (
        g[2].parent == 1 and g[4] == 3 and
        g[5] == 3
    )
    """
    output_nodes = {}
    
    
    try:
        output_nodes[2]
    except KeyError:
        pass
    else:
        raise Exception("should have bombed")
    return output_nodes

first output:
	(1, [(2)])
	(2, [])
	(3, [(4), (5)])
	(4, [])
	(5, [(6),(7)])
	(6, [])
	(7, [])
second output: 
	(1, [(2)])
	(2, [])
	(3, [(4), (5, [(6),(7)])])
	(4, [])
	(6, [])
	(7, [])
	
assert output[n1] == [n2]
assertKeyError     
for node in nodes: 
		gather_nodes()
		
def gather_nodes(node, res:
		if node.visit:
			return
		node.visit = True
		res += [node]
	
	for each child of node: 
		print_node(child.key)

clas			
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