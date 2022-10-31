import singly_linked_list as sll

class foo:
    def bar(self):
        pass
class SortedLinkedList(sll.MyList):
    def insert(self, key):
        if self.head:
            v = self._find_largest_el_smaller_than_key(key)
            wp = sll.MyList.Node(key)
            if not v:
                wp.next = self.head
                self.head = wp
            else:
                wp.next = v.next
                v.next = wp
        else: 
            super().insert(key)
    def _find_largest_el_smaller_than_key(self, key):
        v = self.head
        prev = None
        while v and v.val < key:
            prev, v = v, v.next
        return prev
            