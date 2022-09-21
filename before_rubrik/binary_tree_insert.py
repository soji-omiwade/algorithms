class BinaryTree:
    class Node:
        def __init__(self,key):
            self.key=key
            self.right=self.left=None
            
    def __init__(self, a):    
        def parent(i):
            return (i-1)//2        
        b=[None]*len(a)
        for i in range(len(a)):
            if b[i] is None:
                b[i]=BinaryTree.Node(a[i])
            pi=parent(i)
            if pi>=0:
                if (i%2)==0:
                    b[pi].right=b[i]
                else:
                    b[pi].left=b[i]
        self.root=b[0]

    
    
b=BinaryTree([1,2,3,42,85,420])
assert b.root.key==1 
assert b.root.right.key==3
assert b.root.right.right is None
assert b.root.right.left.key==420
assert b.root.left.left.key==42