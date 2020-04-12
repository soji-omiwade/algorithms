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
        
        def bfs_path_len(g, u, v):
            from collections import deque
            depth = 0
            q = deque([u])
            breadth_count = 1
            while q:
                for _ in range(breadth_count):
                    w = q.popleft()
                    if w is v:
                        q = None
                        break
                    breadth_count = 0
                    for nw in g[w]:
                        q.append(nw)
                        breadth_count += 1
                    depth += 1                
            return depth
            
        paths = set([])
        max_path_len = 0
        from collections import defaultdict
        g = defaultdict(list)
        graph_from_tree(g, root)
        for v, v_nbs in g.items():
            for u in v_nbs:
                if (u,v) not in paths:
                    curr_len = bfs_path_len(g, v, u)
                    max_path_len = max(max_path_len, curr_len)
                    paths.add((u,v))
                    paths.add((v,u))
        return max_path_len
                        
from treebuilder import buildtree
root = buildtree([1,2,3,4,5])
assert Solution().diameterOfBinaryTree(root) == 3
arr = [1,2,3,4,5,None,None,6,None,None,7,8,None,None,9]
root = buildtree(arr)
#assert tree was built right.  do the serialize/deserialize problem!
assert Solution().diameterOfBinaryTree(root) == 6
