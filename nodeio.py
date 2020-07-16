#cleaning the output exercise:-)
from typing import List, Dict
import json
class Node:
    def __init__(self, val, parent=None):
        self.val = val
        self.parent = parent
        self.children = []
        self.visited = False

def get_nodes_from_json_str(json_str):
    nodes = {}
    for item in json.loads(json_str):
        try: 
            parentid = item["parent"]["id"]
        except KeyError:
            parent = None
        else:
            parent = nodes[parentid]
        nodes[item["id"]] = Node(item["id"], parent)
    return nodes
        
def clean_rootlist(rootlist)->None:
    def dfs_helper(sublist:List):
        for lnidx, listnode in enumerate(sublist):
            if listnode[1] == []:
                sublist[lnidx] = listnode[0]
            else:
                dfs_helper(listnode[1])
    dfs_helper(rootlist)

def get_json_output_from_cleanlist(cleanlist)->str:
    """
    output = 
    [
      {
        "id": "0",
      },
      {
        "id": "1",
        "children": [
          {
            "id": "2"
          }
        ]
      },
      {
        "id": "3",
        "children": [
          {
            "id": "4"
          }, 
          {
            "id": "5"
          }
        ]
      }
    ]  
    cleanlist == [0, (1,[2]), (3, [4,(5,[6,7])])]
    """
    def dfs_helper(cleanlist:List)->List[Dict]:
        res = []
        for node in cleanlist:
            if type(node) is int:
                res += [{"id": str(node)}]
            else:
                assert type(node) is tuple
                res += [{"id": str(node[0]), "children": dfs_helper(node[1])}]
        return res
    return json.dumps(dfs_helper(cleanlist), indent=4)