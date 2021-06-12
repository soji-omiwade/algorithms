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
    class BST:
        def __init__(self):
            self.root = None    
            
        def __iter__(self):
            return self.inorder(self.root)
            
        def clear(self):
            self.root = None

        def inorder(self, curr):
            if curr:
                yield from self.inorder(curr.left)
                yield curr.val
                yield from self.inorder(curr.right)            

        class Node:
            def __init__(self, val):
                self.val = val
                self.left = self.right = None

    class DLL:
        class Node:
            def __init__(self, from_, to):
                self.val = (from_, to)
                self.prev = self.next_ = None
                
        def __init__(self):
            self.prehead = Intervals.DLL.Node(float("-inf"), float("-inf"))
            self.posttail= Intervals.DLL.Node(float("inf"), float("inf"))
            self.prehead.next_ = self.posttail
            self.posttail.prev = self.prehead
                  
        def __repr__(self):
            res = []
            curr = self.prehead.next_
            while curr is not self.posttail:
                res.append(curr.val)
                curr = curr.next_
            return str(res)
            
        def clear(self):
            self.prehead.next_ = self.posttail
            self.posttail.prev = self.prehead           
            
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
        
    @classmethod
    def init_as_dll(cls):
        intervals = cls()
        intervals.ints = Intervals.DLL()
        return intervals

    @classmethod
    def init_as_bst(cls):
        intervals = cls()
        intervals.ints = Intervals.BST()
        return intervals
        
    @staticmethod
    def _intersects(top, bot):
        return min(top[1], bot[1]) > max(top[0], bot[0])
        
    def clear(self):
        self.ints.clear()
        
    def addInterval(self, *args):
        if type(self.ints) is list:
            self.addInterval_list(*args)
        elif type(self.ints) is set:
            self.addInterval_set(*args)
        elif type(self.ints) is self.DLL:
            self.addInterval_DLL(*args)
        elif type(self.ints) is self.BST:
            self.addInterval_BST(*args)
        else:
            raise NotImplementedError()
        
    def addInterval_list(self, from_, to):
        '''
        what is going on?! now realizing this won't work if there's stuff in
        between that is not part of i. in which case the ff problems arise:
        - u dont get to nullify the correct location
        - u nullified a location you shouldn't 
        code breaking example:
        (1, 2), (50, 67), (10, 11), (1, 11)
        
        [(1,11), (50,67), (10, 11), (1,11)]
        expected: 10 + 7 = 17
        would get: ... just fixed the code, and now it's much simpler
        '''
        for i, (from_curr, to_curr) in enumerate(self.ints): #O(n)
            if self._intersects((from_, to), (from_curr, to_curr)):
                from_, to = min(from_, from_curr), max(to, to_curr)
                self.ints[i] = None
        self.ints.append((from_, to))
        self.ints = [int_ for int_ in self.ints if int_]           

    def addInterval_set(self, from_, to):
        '''
        this is wrong: the code above shows how to do it right.
        failing case.
        order of incoming intervals: (1, 3), (9, 11), (2, 10)
        expected: 11
        (1, 3)
        (9, 11) 
        (2, 10)--> 
                --> from_,to is now (1, 10) after iterating on (1,3)
                --> now iterate on (9, 11). at ln 86, f, t =  join (1, 10)  and (9, 11) --> (1, 11). But already we added  (1, 10) to the set!
                --> so like above, from_, to, should not forget the last item that was added and check that it isn't a subset of it. 
                --> suffices to check intersect. but what we really need to do here (and in addInterval_list) is check subset!
        code below will have (1, 11) and (2
        '''
        for from_curr, to_curr in self.ints.copy(): #O(n)
            if self._intersects((from_, to), (from_curr, to_curr)):
                from_, to = min(from_, from_curr), max(to, to_curr)
                self.ints.remove((from_curr, to_curr))
        self.ints.add((from_, to))

    def addInterval_set_lite(self, from_, to):
        '''
        ---
              ----
                           ---
           ---------
        type of ints as set
        to_remove as set
        for each int_ in ints:
            if from_, to intersect with int_
                to_remove.add(int_)
                from_, to = union_of(int_, from_, to)
        remove all items in to_remove from ints
        add from_, to to ints
        input_ = ((8, 9), (1, 6), (4, 5), (1, 9))
        res = (1, 6, 6, 8)
        '''
        ints_to_remove = set()
        for int_ in self.ints:
            if self._intersects((from_, to), int_):
                ints_to_remove.add(int_)
                from_, to = min(from_, int_[0]), max(to, int_[1])
        self.ints = self.ints.difference(ints_to_remove)
        self.ints.add((from_, to))
        
    def addInterval_DLL(self, from_, to):
        '''
           i        
        -infph 1 5 9 24 42 inf-pt
        keep moving until intersection or curr is future (if so stop)
        for intersection case:
            modify curr to be extension of new and curr
        for future case:
            get prev of curr
            and fit new in between
        '''           
        curr = self.ints.prehead.next_
        while True:
            if self._intersects(curr.val, (from_, to)):
                #include curr in new item
                from_, to = min(curr.val[0], from_), max(curr.val[1], to)
                #delete curr
                pcurr = curr.prev
                ncurr = curr.next_
                pcurr.next_ = ncurr
                ncurr.prev = pcurr
            elif (from_, to) < curr.val:
                #insert new node, nitem between curr and its prev
                nitem = self.ints.Node(from_, to)
                prev = curr.prev
                curr.prev = prev.next_ = nitem
                nitem.prev = prev
                nitem.next_ = curr
                break
            curr = curr.next_
    
    def addInterval_BST(self, from_, to):
        def get_parent(from_, to):
            curr = self.ints.root
            parent = None
            while curr:
                parent = curr
                if (from_, to) < curr.val:
                    curr = curr.left
                else:
                    curr = curr.right
            return parent
         
        if not self.ints.root:
            self.ints.root = Intervals.BST.Node((from_, to))
        else:
            parent = get_parent(from_, to)
            if (from_, to) < parent.val:
                parent.left = Intervals.BST.Node((from_, to))
            else:
                parent.right = Intervals.BST.Node((from_, to))            

    def getTotalCoveredLengthOverlapping_via_yield(self):
        nolints = []
        for i, int_ in enumerate(self.ints):
            if nolints and self._intersects(nolints[-1], int_):
                nolints[-1] = min(nolints[-1][0], int_[0]), max(nolints[-1][1], int_[1])
            else:
                nolints.append(int_)
        return sum(to - from_ for (from_, to) in nolints)
        
    def getTotalCoveredLengthOverlapping(self):
        def helper(curr):
            if curr:
                helper(curr.left)
                action(curr.val)
                helper(curr.right)

        def action(int_):
            if nolints and self._intersects(nolints[-1], int_):
                nolints[-1] = min(nolints[-1][0], int_[0]), max(nolints[-1][1], int_[1])
            else:
                nolints.append(int_)

        nolints = []
        helper(self.ints.root)
        return sum(to - from_ for (from_, to) in nolints)

    def getTotalCoveredLengthDLL(self) -> int:
        curr = self.ints.prehead.next_
        sum_ = 0
        while curr is not self.ints.posttail:
            sum_ += curr.val[1] - curr.val[0]
            curr = curr.next_
        return sum_
        
    def getTotalCoveredLength(self) -> int:
        if type(self.ints) is Intervals.DLL:
            return self.getTotalCoveredLengthDLL()
        if type(self.ints) is Intervals.BST:
            return self.getTotalCoveredLengthOverlapping()
        reslen = 0
        for (from_, to) in self.ints:
            reslen += to - from_
        return reslen    

