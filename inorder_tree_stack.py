'''

  
    5
   / \
  2   7
st: [5 ] 
curr 5
res [2 ]

if 5 has left
    save 5
    add 5 left

start: 7:58
end: 
'''    
class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.left = left
        self.right = right
        self.val = val
        
'''
push root
push root.left
root = root.left
push root.left
pop into root and process root since it has no more left
no right so ...?
pop into root and process root

push right 
push left again until dead end then go to 35
    5
   /   \
  2     7
 /  \    \
1    4    8
   / \
  3   5

     5
   /   \
  2     7
 /       \
1         8
'''
def inorder(root):
    res = []
    st.append(root)
    while not st:
        if root:
            st.append(root)
            root = root.left
        else:
            root = st.pop()
            process root
            
        process root
        pop
        
    
        while root.left:
            st.append(root.left)
        process(root)
        while  
        root = st.pop()
        
        if root.right:
            st.append(root.right)
    '''
    while not st:
        
        
        
        
        while root.left:
            st.push root-left
        root st.pop
        process val
        while root.right:
            st.push root-right
    '''
    while not st:
        curr = st.pop()
        if curr.left:
            st.append(curr.left)
        else:
            curr = st.pop()
            res.append(curr.val)
            if curr.right:
                st.append(curr.right)
    return res
    
