# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        def listtoarr(head):
            arr = []
            while head:
                arr.append(head)
                head = head.next
            return arr
            
        def helper(arr, lo: int, hi: int) -> TreeNode:
            if lo > hi:
                return None
            mid = (lo + hi) // 2
            curr = TreeNode(arr[mid].val)
            curr.left = helper(arr, lo, mid - 1)
            curr.right = helper(arr, mid + 1, hi)
            return curr
            
        arr = listtoarr(head)
        return helper(arr, 0, len(arr)-1)
        
def isequal(t1:TreeNode, t2: TreeNode) -> bool:
    if (t1 and not t2) or (t2 and not t1):
        return False
    if t1 is t2 is None:
        return True
    if (t1.val == t2.val 
        and isequal(t1.left, t2.left) 
        and isequal(t1.right, t2.right)
        ):
        return True

lis = ListNode(-5, ListNode(2, ListNode(4)))
exp = Solution().sortedListToBST(lis)
act = TreeNode(2, TreeNode(-5), TreeNode(4))
assert isequal(exp, act)