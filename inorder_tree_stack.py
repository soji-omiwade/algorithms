'''
    5
   / \
  2   7
   \
    4
    
    5
   / \
  2   7
st: [5 ] 
curr 5
res [2 ]

if 5 has left
    save 5
    add 5 left

'''    
class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.left = left
        self.right = right
        self.val = val
        
def inorder(root):
    res = []
    st.append(root)
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