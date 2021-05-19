def construct_hierarchy(child_parent:Dict):
    res = []
    
    return res
    
res = construct_hierarchy(tree)
assert res[0][0] == 2
children = res[0][1]
assert children[0][0] == 5
assert children[0][1] == 7

children =  children[0][1]
