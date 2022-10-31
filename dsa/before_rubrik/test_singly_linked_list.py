from singly_linked_list import MyList
import unittest

class ListTestCase(unittest.TestCase):
    def test_single_el_creation(self):
        ml = MyList()
        self.assertEqual(ml.to_list(), [])
        ml.insert(42)
        ml.insert(23)
        self.assertEqual(ml.to_list(), [23,42])
    def test_list_as_string(self):
        foo = [42, 8, 9, 20, 17]
        ml = MyList()
        for x in foo:
            ml.insert(x)
        self.assertEqual(ml.to_list(), foo[-1::-1])
    def test_simple_delete(self):
        foo = [42, 8, 9, 20, 17]
        ml = MyList()
        for x in foo:
            ml.insert(x)
        self.assertEqual(ml.delete(8).val, 8)
        self.assertEqual(ml.delete(420), None)
        ml.delete(20)
        del foo[1]# 8
        del foo[2] #20
        self.assertEqual(ml.to_list(), foo[-1::-1])
    def test_update(self):
        foo = [42, 8, 9, 20, 17]
        ml = MyList()
        for x in foo:
            ml.insert(x)
        self.assertEqual(ml.delete(8).val, 8)
        self.assertEqual(ml.delete(420), None)
        ml.delete(20)
        del foo[1]# 8
        del foo[2] #20
        self.assertEqual(ml.to_list(), foo[-1::-1])
        bar = ml.head.next
        ml.update(bar, 999)
        foo[1] = 999
        self.assertEqual(ml.to_list(), foo[-1::-1])
        
if __name__ == '__main__':
    unittest.main()