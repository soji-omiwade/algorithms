'''
Question : 1
    
    
public interface Intervals {
 
    /**
     * Adds an interval [from, to) into an internal structure.
     */
    void addInterval(int from, int to);
 
    /**
     * Returns a total length covered by the added intervals.
     * If several intervals intersect, the intersection should be counted only once.
     * Example:
     *
     * addInterval(3, 6)
     * addInterval(8, 9)
     * addInterval(1, 5)
     
        addInterval(4, 5)
     *
     * getTotalCoveredLength() -> 6
     *
     * i.e. [1,5) and [3,6) intersect and give a total covered interval [1,6) with a length of 5.
     *      [1,6) and [8,9) don't intersect, so the total covered length is a sum of both intervals, that is 5+1=6.
     *          *f     *t       
     *          |__|__|__|                  
     *                         |__|         (8,9) 
     *    |__|__|__|__|                     (1,6) 
                                            (4,5)
     *
     * 0  1  2  3  4  5  6  7  8  9  10
     *
     */ 
    int getTotalCoveredLength();
 
}
'''
from typing import Tuple, Set
class Intervals:
    def __init__(self):
        self.non_overlapping = set([])
        
    def addInterval(self, from_, to):
        def intersects(from0, to0, from1, to1):
            '''
               ------
                         -----------
            '''
            return min(to0, to1) > max(from0, from1)
            
        '''
        no = {}
                              --
              ----------
                   ----
        '''
        non_overlapping = [list(item) for item in self.non_overlapping]
        non_overlapping.append([from_, to])
        for elem in non_overlapping: #O(n)
            if intersects(from_, to, elem[0], elem[1]):
                from_, to = elem[0], elem[1] = min(from_, elem[0]), max(to, elem[1])
        self.non_overlapping = {tuple(item) for item in non_overlapping}

    def getTotalCoveredLength(self) -> int:
        reslen = 0
        for (from_, to) in self.non_overlapping:
            reslen += (to - from_)
        return reslen    

intervals = Intervals()       
intervals.addInterval(8, 9)
assert intervals.getTotalCoveredLength() == 1
intervals.addInterval(1, 6)
assert intervals.getTotalCoveredLength() == 6
intervals.addInterval(4, 5)
assert intervals.getTotalCoveredLength() == 6
intervals.addInterval(1, 9)
assert intervals.getTotalCoveredLength() == 8


    
'''
    Question # 2:
    
    
    Design an algorithm and write code to serialize and deserialize a binary tree. Writing the tree to a file is called ‘serialization’ and reading back from the file to reconstruct the exact same binary tree is ‘deserialization’. Assume that every node has an integer value.
        
    

            
    a     1
 b     c    2
n  n  n   d   4
a, b, c, n, n, n, d  8 

from collections import deque
nodes = deque([root])
count = 1
while nodes:
    for i in range(count):
        
        node = nodes.popleft()
        if not node:
            write(None)
        else:
            write(node.val)
            nodes.append(node.left)
            nodes.append(node.right)
    count = count * 2

    
    public class BinaryTree {
 
    private Node root;
 
    private static class Node {
        int data;
        Node left;
        Node right;
    }
 
    /**
     * Write the serialized form of this tree into the given stream.
     */
    public void serialize(OutputStream into) throws IOException {
        // implement this
    }
 
    /**
     * Reconstruct a tree from its serialized form.
     */
    public static BinaryTree deserialize(InputStream from) {
        // implement this
    }
}
'''