# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        def foo():
            pass
        if not root:
            return []        
        res=[[]]
        from queue import deque
        q=deque()
        q.append(root)
        q.append(None)
        while q:
            v=q.popleft()
            if v:
                res[len(res)-1].append(v.val)
                if v.left:
                    q.append(v.left)
                if v.right:
                    q.append(v.right)
            else:
                if len(q)>0:
                    res.append([])
                    q.append(None)
        return res

def build_tree(tl):
    d={}
    root=TreeNode(tl[0])
    d[0]=root
    for i in range(len(tl)):
        v=d[i]
        if v and 2*i+1<len(tl):
            v.left=None
            if tl[2*i+1] is not None:
                v.left=TreeNode(tl[2*i+1])
            v.right=None
            if tl[2*i+2] is not None:
                v.right=TreeNode(tl[2*i+2])
            d[2*i+1]=v.left
            d[2*i+2]=v.right
    return root

assert(
print(Solution().levelOrder(build_tree([3,9,20,None,None,15,7])))
assert (Solution().levelOrder(build_tree([3,9,20,None,None,15,7])) == 
        [[3],[9,20],[15,7]])
