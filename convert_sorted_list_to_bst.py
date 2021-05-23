#time: 9:42pm
#time end: 10:18
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
        def midelement(lo: ListNode, hix: ListNode) -> ListNode:
            slow = fast = lo
            while fast is not hix and fast.next is not hix:
                fast = fast.next.next
                slow = slow.next
            return slow
        
        def helper(lo: ListNode, hix: ListNode) -> TreeNode:
            if lo is hix:
                return None
            lisnode = midelement(lo, hix) #3-list
            treenode = TreeNode(lisnode.val) #3-bst
            treenode.left = helper(lo, lisnode)
            treenode.right = helper(lisnode.next, hix)
            return treenode
            
        return helper(head, None)
        
lis = ListNode(1, ListNode(2, ListNode(3)))
res = Solution().sortedListToBST(lis)
assert (res.val == 2
        and res.left.val == 1
        and res.right.val == 3)
        
lis = ListNode(1, ListNode(2))
res = Solution().sortedListToBST(lis)
assert (res.val == 2
        and res.left.val == 1)