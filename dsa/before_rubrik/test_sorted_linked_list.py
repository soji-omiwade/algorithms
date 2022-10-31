from sorted_linked_list import SortedLinkedList
import unittest
class TestCase(unittest.TestCase):
    def test(self):
        mylist = SortedLinkedList()
        mylist.insert(5)
        mylist.insert(9)
        mylist.insert(1)
        mylist.insert(8)
        mylist.insert(7)
        self.assertEqual(mylist.to_list(), [1,5,7,8,9])
        
if __name__ == "__main__":
    unittest.main()