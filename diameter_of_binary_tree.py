from treenode import TreeNode
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        """procedure: 
        - create a graph from the tree
        - find shortest path (bfs) for u to v for all u to v
        - return the length of shortest path
        """
        def graph_from_tree(g, v):
            """takes the root node of a bst and 
            turns it into a graph (adjacencey list wise)
            """
            if v.left:
                g[v.val].append(v.left.val)
                g[v.left.val].append(v.val)
                graph_from_tree(g, v.left)
            if v.right:
                g[v.val].append(v.right.val)
                g[v.right.val].append(v.val)
                graph_from_tree(g, v.right)
        
        def bfs_path_len(g, s, t):
            from collections import deque
            depth = 0
            q = deque([s])
            breadth = 1
            visit = defaultdict(bool)
            while q:
                """loop invariant:
                at beginning of while
                depth: we are about to process nodes at depth depth
                breadth: number of nodes at depth above
                next_breadth:used to set breadth
                """
                next_breadth = 0
                for _ in range(breadth):
                    v = q.popleft()
                    if v == t:
                        return depth
                    for nv in g[v]:
                        if not visit[nv]:
                            q.append(nv)
                            next_breadth += 1
                    visit[v] = True
                breadth = next_breadth
                depth += 1
            raise Exception(f"path from {s} to {t} not found")
            
        paths = set([])
        max_path_len = 0
        from collections import defaultdict
        g = defaultdict(list)
        graph_from_tree(g, root)
        for u in g:
            for v in g:
                if u is not v and (u,v) not in paths:
                    curr_len = bfs_path_len(g, u, v)
                    max_path_len = max(max_path_len, curr_len)
                    paths.add((u,v))
                    paths.add((v,u))
        return max_path_len
                        
from treebuilder import buildtree
root = buildtree([1,2,3,4,5])
print(Solution().diameterOfBinaryTree(root))
assert Solution().diameterOfBinaryTree(root) == 3

arr = [1,2,3,4,5,None,None,6,None,None,7,8,None,None,9]
root = buildtree(arr)
three = root.right
two = root.left
six = two.left.left
seven = two.right.right
assert six.val == 6
assert seven.val == 7
assert three.val == 3
assert six.left.val == 8
assert seven.right.val == 9
assert six.right is seven.left is None

# assert Solution().diameterOfBinaryTree(root) == 6
