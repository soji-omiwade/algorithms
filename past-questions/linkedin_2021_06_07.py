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
         self.ints = None

    @classmethod
    def init_as_set(cls):
        intervals = cls()
        intervals.ints = set([])
        return intervals
        
    @classmethod
    def init_as_list(cls):
        intervals = cls()
        intervals.ints = []
        return intervals
        
    @staticmethod
    def _intersects(top, bot):
        return min(top[1], bot[1]) > max(top[0], bot[0])
        
    def addInterval_list(self, from_, to):
        self.ints.append((from_, to))
        for i, (from_curr, to_curr) in enumerate(self.ints): #O(n)
            if self._intersects((from_, to), (from_curr, to_curr)):
                from_, to = min(from_, from_curr), max(to, to_curr)
                if i > 0 and self._intersects(self.ints[i - 1], (from_, to)):
                    self.ints[i - 1] = None
                self.ints[i] = from_, to
        self.ints = [int_ for int_ in self.ints if int_]           

    def addInterval_set(self, from_, to):
        self.ints.add((from_, to))
        for from_curr, to_curr in self.ints.copy(): #O(n)
            if self._intersects((from_, to), (from_curr, to_curr)):
                from_, to = min(from_, from_curr), max(to, to_curr)
                self.ints.remove((from_curr, to_curr))
                self.ints.add((from_, to))
    # def addInterval_heap(self, e
    def getTotalCoveredLength(self) -> int:
        reslen = 0
        for (from_, to) in self.ints:
            reslen += to - from_
        return reslen    

intervals = Intervals.init_as_set()       
intervals.addInterval_set(8, 9)
assert intervals.getTotalCoveredLength() == 1
intervals.addInterval_set(1, 6)
assert intervals.getTotalCoveredLength() == 6
intervals.addInterval_set(4, 5)
assert intervals.getTotalCoveredLength() == 6
intervals.addInterval_set(1, 9)
assert intervals.getTotalCoveredLength() == 8

intervals = Intervals.init_as_list()       
intervals.addInterval_list(8, 9)
assert intervals.getTotalCoveredLength() == 1
intervals.addInterval_list(1, 6)
assert intervals.getTotalCoveredLength() == 6
intervals.addInterval_list(4, 5)
print(intervals.getTotalCoveredLength())
print(intervals.ints)
assert intervals.getTotalCoveredLength() == 6
intervals.addInterval_list(1, 9)
assert intervals.getTotalCoveredLength() == 8

# intervals = Intervals()       
# intervals.addInterval_heap(8, 9)
# assert intervals.getTotalCoveredLength() == 1
# intervals.addInterval_heap(1, 6)
# assert intervals.getTotalCoveredLength() == 6
# intervals.addInterval_heap(4, 5)
# assert intervals.getTotalCoveredLength() == 6
# intervals.addInterval_heap(1, 9)
# assert intervals.getTotalCoveredLength() == 8


    
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