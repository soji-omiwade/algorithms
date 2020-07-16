from nodeio import (
    get_nodes_from_json_str, 
    clean_rootlist, 
    get_json_output_from_cleanlist
    )
  
def set_children(nodes):
    for v in nodes.values():
        if v.parent:
            nodes[v.parent.val].children += [v]
            
def get_descs(v):
    v.visited = True
    v_descs = []
    for w in v.children:
        v_descs.append((int(w.val), get_descs(w)))
    return v_descs

def construct_hierarchy(nodes):
    set_children(nodes)
    rootlist = []
    for v in nodes.values():
        if not v.visited and not v.parent:
            rootlist.append((int(v.val), get_descs(v)))
    return rootlist

#testcase 1
input_str = """
[
    { "id": "1" },
    { "id": "2", "parent": { "id": "1" } },
    { "id": "3" },
    { "id": "4", "parent": { "id": "3" } },
    { "id": "5", "parent": { "id": "3" } }
]
"""
nodes = get_nodes_from_json_str(input_str)
assert construct_hierarchy(nodes) == [(1, [(2, [])]), (3, [(4,[]), (5,[])])]


#testcase 2
input_str = """
[
    { "id": "1" },
    { "id": "2", "parent": { "id": "1" } },
    { "id": "3" },
    { "id": "4", "parent": { "id": "3" } },
    { "id": "5", "parent": { "id": "3" } },
    { "id": "6", "parent": { "id": "5" } },
    { "id": "7", "parent": { "id": "5" } }
]
"""
nodes = get_nodes_from_json_str(input_str)
hierarchy = construct_hierarchy(nodes)
assert (hierarchy == [
        (1, [
            (2, [])]), 
        (3, [
                (4,[]), 
                (5,[
                    (6,[]),
                    (7, [])])])])
clean_rootlist(hierarchy)
assert (hierarchy == [(1,[2]), (3, [4,(5,[6,7])])])

output = """[
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
        "id": "5",
        "children": [
          {
            "id": "6"
          },
          {
            "id": "7"
          }
        ]
      }
    ]
  }
]
"""
json_output = get_json_output_from_cleanlist(hierarchy)

for i, line1, line2 in zip(range(len(output.splitlines())), 
    json_output.splitlines(), output.splitlines()):
    print(len(line1) - len(line2))
    try:
        assert line1.strip() == line2.strip()
    except AssertionError:
        raise Exception(f"Line {i}: {line1.strip()} and {line2.strip()} unequal")