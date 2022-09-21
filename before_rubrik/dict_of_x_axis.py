import unittest
from collections import defaultdict

def go(root): 
    d = defaultdict(list)
    def dfs(x, pos):
        if x:
            d[pos].append(x.key)
            dfs(x.left, pos-1)
            dfs(x.right, pos+1)
    dfs(root, 0)
    #d = {1:[3,42], -1:[2], 0:[1]}
    res = []
    for val in sorted(d.items()):
        res.append(val[1])
    return res
    
    
class TreeNode:
    def __init__(self, key, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right
        
class TestCase(unittest.TestCase):
    def test(self):
        self.assertEqual(go(
            TreeNode(1,
            TreeNode(2, TreeNode(4), TreeNode(5)), 
            TreeNode(3, TreeNode(6), TreeNode(7)))),
            [[4],[2],[1,5,6],[3],[7]])
    def test_other(self):
        self.assertEqual(go(TreeNode(1, TreeNode(2), TreeNode(3))),
            [[2],[1],[3]])
        
if __name__ == '__main__':
    unittest.main(verbosity=2)
    
    
#resume for Tolu when done.
