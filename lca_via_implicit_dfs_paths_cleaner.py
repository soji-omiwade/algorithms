from math import inf
class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right
        
    def __str__(self):
        return str(self.val) + ": " + super().__str__()
    
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode', needed=2) -> 'TreeNode':
        def dfs(v, p, q, needed):
            if not v or not needed:
                return 0, None
            visited.add(v)
            herecount = int(v in (p, q))
            leftcount, resleft = dfs(v.left, p, q, needed - herecount)
            rightcount, resright = dfs(v.right, p, q, needed - herecount - leftcount)
            allcount = herecount + leftcount + rightcount
            res = None
            if 2 in (leftcount, rightcount):
                res = resleft or resright
            elif allcount == 2:
                res = v
            return allcount, res                
            
        return dfs(root, p, q, needed)[1]
        
n10 = TreeNode(10)
n6 = TreeNode(6)
n3 = TreeNode(3, n6, TreeNode(7,None,n10))
n9 = TreeNode(9)
n8 = TreeNode(8)
n5 = TreeNode(5, n8, n9)
n4 = TreeNode(4)
n2 = TreeNode(2, n4, n5)
n1 = TreeNode(1, n2, n3)
visited = set([])
assert Solution().lowestCommonAncestor(n5, n8, n9, inf) is n5
assert len(visited) == 3; visited = set([])
assert Solution().lowestCommonAncestor(n3, n3, n10, inf) is n3
assert len(visited) == 4; visited = set([])
assert Solution().lowestCommonAncestor(n1, n3, n10, inf) is n3
assert len(visited) == 10; visited = set([])
assert Solution().lowestCommonAncestor(n1, n9, n6, inf) is n1
assert len(visited) == 10; visited = set([])
assert Solution().lowestCommonAncestor(n1, n4, n9, inf) is n2
assert len(visited) == 10; visited = set([])

visited = set([])
assert Solution().lowestCommonAncestor(n5, n8, n9) is n5
assert len(visited) == 3; visited = set([])
assert Solution().lowestCommonAncestor(n3, n3, n10) is n3
assert len(visited) == 4; visited = set([])
assert Solution().lowestCommonAncestor(n1, n3, n10) is n3
assert len(visited) == 10; visited = set([])
assert Solution().lowestCommonAncestor(n1, n9, n6) is n1
assert len(visited) == 8; visited = set([])
assert Solution().lowestCommonAncestor(n1, n4, n9) is n2
assert len(visited) == 6; visited = set([])


