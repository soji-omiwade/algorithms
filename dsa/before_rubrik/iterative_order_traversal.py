'''
    5
  1    2 
3     7   9



st = 5 1 3 
process: pop&proc 3 pop 1
'''

def inorder(root):
    res = []
    st = [] 
    while True:
        if root:
            st.append(root)
            root = root.left
        else:
            if not st:
                break
            root = st.pop()
            res.append(root.val)
            root = root.right
    return res
    
'''
    5
  1    2 
3     7   9
'''
def preorder(root):
    res = []
    st = [] 
    while True:
        if root:
            st.append(root)
            res.append(root.val)            
            root = root.left
        else:
            if not st:
                break
            root = st.pop()
            root = root.right
    return res

'''
    5
  1    2 
3     7   9

st 1 7  
root 5 2 9 
'''
def postorder(root):
    res = []
    st = [root]
    other = []
    while st:
        root = st.pop()
        other.append(root.val)
        if root.left:
            st.append(root.left)
        if root.right:
            st.append(root.right)
    return other[::-1]
    
class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
root = TreeNode(5, 
            TreeNode(1, TreeNode(3)), 
            TreeNode(2, TreeNode(7), TreeNode(9)))
'''
    5
  1    2 
3     7   9
'''
print(inorder(root)) #3, 1, 5 7 2 9
print(preorder(root)) #5 1 3 2 7 9
print(postorder(root)) #3 1 7 9 2 5

