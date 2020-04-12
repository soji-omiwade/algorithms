# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class List:
    def __init__(self, *arr):
        self.prehead = ListNode(float("-inf"))
        self.posttail = ListNode(float("inf"))
        self.prehead.next, self.posttail.next = self.posttail, self.prehead
        for x in arr:
            v = ListNode(x)
            self.posttail.next.next = v
            v.next, self.posttail.next = self.posttail, v
    def serialize(self):
        arr = []
        v = self.prehead.next
        while v is not self.posttail:
            arr.append(v.val)
            v = v.next
        return arr

arr = [i+42 for i in range(10)]
lis = List(*arr)
assert lis.serialize() == arr
assert lis.serialize() is not arr

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        if head is None:
            return None
        slow = fast = head
        while fast.val != float("inf") and fast.next.val != float("inf"):
            slow = slow.next
            fast = fast.next.next
        return slow
        
if __name__ == "__main__":
    mlist = List(1,3,5,7,9)
    middle = mlist.prehead.next.next.next
    assert Solution().middleNode(mlist.prehead.next) is middle

    mlist = List(1,3,15,17,9,10,4,42,10,23)
    middle = mlist.prehead.next.next.next.next.next.next
    assert Solution().middleNode(mlist.prehead.next) is middle    