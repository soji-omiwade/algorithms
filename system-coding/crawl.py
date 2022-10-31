from typing import Set, List

def bfs_crawl(seeds: List[str], max_depth: int) -> Set[str]:
    pass

'''
     root
     1  2  3  4 --- d = 1
'''
def dfs_crawl(seeds: List[str], max_depth: int) -> Set[str]:
    visited = set()
    for seed in seeds:
        helper_crawl(seed, max_depth)

def helper_crawl(node, depth, visited):
    if depth == 0 or node in visited:
        return
    visited.add(node)
    nodes = get_neighbors(node)
    for node in nodes:
        if node not in visited:
            crawl(node, depth - 1)

results = crawl(seeds, max_depth)
