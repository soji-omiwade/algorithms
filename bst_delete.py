def delete(self, node) -> None:
    
    def slidedownleft(node, isleft):
        while node.left.left is not None:
            nodeleft = node.left
            pinode = pi[node]
            
            pinode.left = nodeleft         
            node.left = nodeleft.left           
            nodeleft.left = node
                    
            pi[nodeleft] = pinode
            pi[node] = nodeleft
            pi[nodeleft.left] = node
        
        nodeleft  = node.left
        pinode = pi[node]
        pinode.left = nodeleft
        node.left = None
            
    def get_needed_parents(node):
        pi
    def slidedown(succ):
        while succ.right:
            #recurse
            succ.left, succright.left = succright.left, succ.left
            succ.right, succright.right = succright.right, succ
            pi[succright], pi[succ] = pi[succ], succright
    pi = get_needed_parents()
    if node.left is node.right is None:
        #remove the leaf item
        if pi[node].left is node:
            pi[node].left = None
        else:
            pi[node].right = None
    else:
        if node.left:
            slidedownleft(node, True)
        else:
            slidedownleft(node, False)
        
    return node

