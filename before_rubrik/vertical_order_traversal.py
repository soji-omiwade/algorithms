# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return None
        res = []
        q = deque([(root, 0, 0)])
        lookup = defaultdict(list)
        minval, maxval = float("inf"), float("-inf")
        while q:
            for i in range(len(q)):
                node, row, col = q.popleft()
                minval, maxval = min(minval, col), max(maxval, col)
                
                #process node here...
                lookup[col].append((row, node.val)) #look
                
                if node.left:
                    q.append((node.left, row + 1, col - 1))
                if node.right:
                    q.append((node.right, row + 1, col + 1))
                    
        for lis in lookup.values():
            lis.sort()
        for i in range(minval, maxval + 1):
            res.append([val for (row, val) in lookup[i]])
        return res