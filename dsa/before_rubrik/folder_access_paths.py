"""
input: 
    tree of folders
    folders uses have access to access which is a subset of nodes in tree
output: 
    given a folder, does the user have access to it?
user has access to folder only if, on a path to the root starting from the node itself, there is a node with access

        A
    B   C   D
   E     G
   F
"""


import unittest
class TestCase(unittest.TestCase):
    def test(self):
        tuples = (
        ('A', None),
        ('B', 'A'),
        ('C', 'A'),
        ('D', 'A'),
        ('G', 'C'),
        ('E', 'B'),
        ('F', 'E'))
        access = ['C', 'G']

        tree = build_tree(tuples, access)
        
        self.assertEqual(go(tree, 'A'), True)
        self.assertEqual(go(tree, 'B'), False)
        self.assertEqual(go(tree, 'C'), True)
        self.assertEqual(go(tree, 'E'), False)
    
from collections import defaultdict
def build_tree(tuples, access):
    tree = defaultdict(list)
    for child,parent in tuples:
        pass
        

def go(tree, folder, v):
    """v is not None"""
    
    a = v.access
    b = False
    if not v.kids:
        b = folder == v.folder
        
    for w in v.kids:
        (a,b) |= go(tree, folder, w)
        
    if 
    return a,b