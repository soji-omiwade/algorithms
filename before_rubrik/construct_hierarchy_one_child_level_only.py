from typing import Dict, List
import json

def helper(parents: Dict[str, str]) -> Dict[str, List]:
    childrens = {}
    for child, parent in parents.items():
        try: 
            childrens[parent].append(child)
        except:
            childrens[parent] = [child]
    return childrens

def constructHierarchy(json_input: str)->str:
    input = json.loads(json_input)
    
    #prepare the input
    parents = {}
    for item in input:
        if len(item) > 1:
            parents[item["id"]] = item["parent"]["id"]
            
    #transform the data
    childrens = helper(parents)
    
    #prepare the output
    output = []
    for parent, children in childrens.items():
        json_children = []
        for child in children:
            json_children += [dict(id=child)]
        output.append(dict(id=parent, children=json_children))
        
    return json.dumps(output, indent=4)  
input = """
  [
    { "id": "1" },
    { "id": "2", "parent": { "id": "1" } },
    { "id": "3" },
    { "id": "4", "parent": { "id": "3" } },
    { "id": "5", "parent": { "id": "3" } }
  ]
"""
output = """
      [
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
"""
print(constructHierarchy(input))