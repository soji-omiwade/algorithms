class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next_ = next
        
def merge_sorted_lists_iterative2(l1, l2):
    curr = head = ListNode(None)
    while l1 and l2:
        if l1.val < l2.val:
            curr.next_ = l1
            l1 = l1.next_
        else:
            curr.next_ = l2
            l2 = l2.next_
            curr.next_.next_ = l1
        curr = curr.next_
    curr.next_ = l2 or l1
    return head.next_

def merge_sorted_lists_iterative1(l1, l2):
    head = curr = ListNode(None)
    while l1 and l2:
        if l1.val < l2.val:
            curr.next_ = l1
            l1 = l1.next_
        else:
            curr.next_ = l2
            l2 = l2.next_
        curr = curr.next_
    curr.next_ = l1 or l2
    return head.next_

def merge_sorted_lists_recursive(l1, l2):
    if not l2:
        return l1
    if not l1:
        return l2
    assert l1 and l2
    if l1.val < l2.val:
        l1.next_ = merge_sorted_lists_recursive(l1.next_, l2)
        return l1
    l2.next_ = merge_sorted_lists_recursive(l2.next_, l1)
    return l2

def arr_to_list(arr):
    head = last = ListNode(None)
    for val in arr:
        last.next_ = ListNode(val)
        last = last.next_
    return head.next_
    
def list_to_arr(node):
    arr = []
    while node:
        arr.append(node.val)
        node = node.next_
    return arr
        
assert list_to_arr(ListNode(5, ListNode(2, ListNode(42)))) == [5, 2, 42]
#regular case -- intersecting
l1 = arr_to_list([i for i in range(0, 20, 2)])
l2 = arr_to_list([i for i in range(1, 20, 2)])
assert [i for i in range(20)] == list_to_arr(merge_sorted_lists_recursive(l1, l2))
#regular case -- not intersecting
l1 = arr_to_list([i for i in range(0, 10)])
l2 = arr_to_list([i for i in range(10, 20)])
assert [i for i in range(20)] == list_to_arr(merge_sorted_lists_recursive(l1, l2))
#boundary cases...
l1 = None
l2 = arr_to_list([i for i in range(1, 20, 2)])
assert [i for i in range(1, 20, 2)] == list_to_arr(merge_sorted_lists_recursive(l1, l2))


assert list_to_arr(ListNode(5, ListNode(2, ListNode(42)))) == [5, 2, 42]
#regular case -- intersecting
l1 = arr_to_list([i for i in range(0, 20, 2)])
l2 = arr_to_list([i for i in range(1, 20, 2)])
assert [i for i in range(20)] == list_to_arr(merge_sorted_lists_iterative1(l1, l2))
#regular case -- not intersecting
l1 = arr_to_list([i for i in range(0, 10)])
l2 = arr_to_list([i for i in range(10, 20)])
assert [i for i in range(20)] == list_to_arr(merge_sorted_lists_iterative1(l1, l2))

#boundary cases...
l1 = None
l2 = arr_to_list([i for i in range(1, 20, 2)])
assert [i for i in range(1, 20, 2)] == list_to_arr(merge_sorted_lists_iterative2(l1, l2))

assert list_to_arr(ListNode(5, ListNode(2, ListNode(42)))) == [5, 2, 42]
#regular case -- intersecting
l1 = arr_to_list([i for i in range(0, 20, 2)])
l2 = arr_to_list([i for i in range(1, 20, 2)])
assert [i for i in range(20)] == list_to_arr(merge_sorted_lists_iterative2(l1, l2))
#regular case -- not intersecting
l1 = arr_to_list([i for i in range(0, 10)])
l2 = arr_to_list([i for i in range(10, 20)])
assert [i for i in range(20)] == list_to_arr(merge_sorted_lists_iterative2(l1, l2))

#boundary cases...
l1 = None
l2 = arr_to_list([i for i in range(1, 20, 2)])
assert [i for i in range(1, 20, 2)] == list_to_arr(merge_sorted_lists_iterative2(l1, l2))
