from collections import deque
from typing import List
from tree_builder import build_tree
from treenode import TreeNode
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        """
        do a level first search. and check that the list on that level 
        is a palindrome
        """
        def is_palindrome(a: List[TreeNode]):
            flag = False
            for i in range(len(a)//2):
                if a[i] != a[len(a)-1-i]:
                    flag = True
                    break
            return not flag        
        queue = deque([root])
        is_pal = True
        while is_pal and queue:
            a = []
            count = len(queue)
            for _ in range(count):
                v = queue.popleft()
                a.append(v.val if v else None)
                if v:
                    queue.append(v.left)
                    queue.append(v.right)
            is_pal = is_palindrome(a)
        return is_pal    
        
            
assert Solution().isSymmetric(None)
tree = build_tree([2,1,1,4,8,8,4])
assert Solution().isSymmetric(tree)
tree = build_tree([2,1,1,4,8,3,4])
assert not Solution().isSymmetric(tree)
tree = build_tree([2,1,1,4,None,8,4])
assert not Solution().isSymmetric(tree)
