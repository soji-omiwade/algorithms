class BinaryTree:
    class Node:
        def __init__(self,key):
            self.key=key
            
    def __init__(self, a):
    
        def left(i):
            return 2*i+1
        def right(i):
            return 2*i+2
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

    
    
b=BinaryTree([1,2,3])
assert b.root.key==1 
assert b.root.right.key==3


