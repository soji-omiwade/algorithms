class BinaryTree:
    class Node:
        def __init__(self,key):
            self.key=key
            
    def __init__(self, a):
        def left(i):
            return 2*i+1
        def right(i):
            return 2*i+2
        
        n=len(a)
        b=[None]*n
        self.root=b[0]=BinaryTree.Node(a[0])
        for i in range(n):
            if left(i) < n:
                b[i].left=b[left(i)]=BinaryTree.Node(a[left(i)])
                if right(i) < n:
                    b[i].right=b[right(i)]=BinaryTree.Node(a[right(i)])              

b=BinaryTree([1,2,3])
assert b.root.key==1 
assert b.root.right.key==3


b=BinaryTree([1,2,3,42,85,420])
assert b.root.key==1 
assert b.root.right.key==3
assert b.root.right.right is None
assert b.root.right.left.key==420
assert b.root.left.left.key==42

