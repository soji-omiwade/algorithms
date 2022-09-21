        '''
Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
Output = []
      3
    /   \
   9    20
       /  \
      15   7
      
output = [
We need a tree that looks like above. 3 is the root, 9 is its left node and so on.
To solve this, let's walk through
- the very first element, 3, in preorder has to be the root; because that's how preorder works
- on the other hand, by how inorder works: we can go to inorder and find the index of 3 (the root)
    - this brings up a key property: all elements must be unique. 
    - otherwise what if we find first a different 3 than the root
- create a treenode(3) (this is the result node  since it is the tree root)
       3
      /  \
- from inorder, it is located in idx 1
- subsequently we know every node in its left and right subtree is [0, 0] and [2, 4] 
- recursively we apply same principle to preorder, but starting from the next down the preorder.
    - we just need to advance to idx 1 
    - so 9 is the root node
    - it will recursively try to do the same
    - idx of 9 is 0. so left and right are (0, -1), and (1, 0)  <--- SHOULD HAVE MENTIONED WE HAVE A STOPPING CONDITION
    - each of these have no nodes. 
    - tree is now
        3
       /  \
      9
    
    
    - get the next preorder array element: 20. 
    - but also remember the interval (from its parent 3) is [2, 4]
    - find it in inorder. to characterize the left and right subtrees
    - make node 20 root. 
       3
      / \
     9   20
    - interval of children of 20: [2, ...] and [..., 4]
    - dots are 3 - 1 and 3  + 1, 3 is idx of 20
     so we have [2, 2] and [4, 4]

    - for the range [2,2] we advance in preorder to get 15  
    - cannot make children with [2, 1], and [3, 2]
    - we are done. 
    
    - for the range [4, 4] 
    - we now advance preorder to pull out the last element 7 
    - find it to be located at 4
    - ranges 7 submits for its children : [4, 3] and [5, 4]  
    - advance preorder. wait we are done. 
        -we are also done because there is no other recursive range to call!

    so we see a pattern of some things from which we glean pseudocode
    
    1) we pop an element from preorder (it is the next subroot we create)
    2) subrootidx = look for it in inorder given a range passed in [inorder_start, inorder_end]
    3) create a subroot(subroot(inorder[subrootidx]))
    4) recursively do 1 with the following ranges: [inorder_start, subrootidx - 1], [subrootidx + 1, inorder_end]
        4a) as a base case we won't do 1 if the interval is empty
        4b) we could consider also when preorder is empty, but I think this is redundant
   
    Time: we advance the tree one time (via preorder). this is O(n)
        but we use (2) to make O(n) complexity each time.
    note: since elements are unique, we can make one pass and get the inorder locations of every value (as akey) into a dictionary
        now we have O(n) total 
    Space: could be O(n) if we copy preorder into a deque to support popleft 
            but we don't need to use a stack. we can just advance idx through preorder
     
        '''
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        def helper(iostart, ioend):
            nonlocal poidx
            if iostart > ioend:  #0,5...
                return None
            poidx += 1            #0
            poval = preorder[poidx]
            subrootidx = ioloc[poval] # 1
            res = TreeNode(poval)
            res.left = helper(iostart, subrootidx - 1)
            res.right = helper(subrootidx + 1, ioend)  # [2,4]
            return res
        poidx = -1
        ioloc = {ioval: idx for (idx, ioval) in enumerate(inorder)}
        return helper(0, len(inorder) - 1)
