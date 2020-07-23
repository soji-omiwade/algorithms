class Node:
    def __init__(self, val):
        self.val = val
        self.nbs = []
        
def dfs_history(rships):
    def dfs_helper(v, count):
        if history[v][0] is not None:
            return count
        count += 1
        print(v.val, count)
        history[v][0] = count
        for w in v.nbs:
            count = dfs_helper(w, count)
        count += 1
        history[v][1] = count
        return count

    nodes = {}
    for idxs in rships:
        for idx in idxs:
            if idx not in nodes:
                nodes[idx] = Node(idx)
        idxs_from_second = iter(idxs);
        idx = next(idxs_from_second);
        for nb_idx in idxs_from_second:
            nodes[idx].nbs += [nodes[nb_idx]] 
            nodes[nb_idx].nbs += [nodes[idx]]
    history = {v:[None,None] for v in nodes.values()} 
    count = -1
    for v in nodes.values():
        count = dfs_helper(v, count)
    history = [(v.val, history[v][0], history[v][1]) for _,v in sorted(nodes.items())]
    return history

rships = [
    [8,9,10],
    [11],
    [1,2,5,3],
    [2,4,5,3],
    [3,6,7],
    [4,5],
]
history = dfs_history(rships)
assert history == [
    (1, 8, 21),
    (2, 9, 20),
    (3,14, 19),
    (4,10, 13),
    (5,11, 12),
    (6,15, 16),
    (7,17, 18),
    (8, 0,  5),
    (9, 1,  2),
    (10, 3,  4),
    (11, 6, 7),
]