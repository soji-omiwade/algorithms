def say_hello():
    print('Hello, World')

for i in range(5):
    say_hello()

'''
Given the head of a singly linked list, reverse the list, and return the reversed list.

 Input: 1->4->6->8->11
 Outpu : 11->8->6->4->1

Example 1:


Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]
Example 2:


Input: head = [1,2]
Output: [2,1]
Example 3:

Input: head = []
Output: []
 

Constraints:

The number of nodes in the list is the range [0, 5000].
-5000 <= Node.val <= 5000

i/o
 Input: 1->4->6->8->11
 Outpu : 11->8->6->4->1

constraints
diagram
null<- 1-> 4-> 6-> <-8 ? 11
h,                       p, c  

1 null
  c
pseudocode

c = head.next
prev = head
head.next = null
for each node curr, c until c is null
  temp = c.next
  c.next = prev
  prev = c
  c = temp
return prev

'''

class ListNode: 
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
        
        
def reverse_list(head: ListNode) -> ListNode:
    '''
    1< 2 3 4   
    if not head
        return null
    nhead = reverse_list_helper(head)
    head.next = None
    def reverse_list_helper(head, head_next)
        if head_next:
            temp = head_next.next # 4
            head.next.next = head
            return reverselist(head.next, temp)
        else:
            return head
    '''
    
    if not head:
        return None
    curr = head.next # 2
    prev = head      # 1
    head.next = None  #1 -> None
    #for each node curr, c until c is null
    while curr:
      temp = curr.next # 3
      curr.next = prev # 2-> 1   3->2
      prev = curr      # 2       3
      curr = temp       # 3      
    return prev

#t: O(n) .. iterate once through the list
#s: O(1) .. no additional linear sized data structure
#head = ListNode(1, ListNode(2, ListNode(3)))
#head = None
#head = ListNode(1)
#head = reverse_list(head)
#while head:
#    print(head.val)
#    head = head.next
    
'''
Given the root of a binary tree, invert the tree, and return its root.



Example 1:


Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]
Example 2:


Input: root = [2,1,3]
Output: [2,3,1]
Example 3:

Input: root = []
Output: []
 

Constraints:

The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


  1
 / \ 
2     3
     / \
    5   6
      
      1
    3   2
   6  
function inverttree(root)
    if not root
        return 
    root.left, root.right = root.right, root.left
    inverttree(root.left)
    inverttree(root.right)
      
'''
# 
# Your previous Plain Text content is preserved below:
# 
# Welcome to your interviewing.io interview.
# 
# Once you and your partner have joined, a voice call will start automatically.
# 
# Use the language dropdown near the top right to select the language you would like to use.
# 
# You can run code by hitting the 'Run' button near the top left.
# 
# Enjoy your interview!
'''
   1
  /  \ 
 2     3
     / \
    5   6

2 - 7 - 8 - 9
              \right
              10

      1
    3   2
   6 5 

s: O(h) - height of the tree 
t: O(n)
'''


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def invert_tree(root: TreeNode) -> None:
    if not root:
        return 
    root.left, root.right = root.right, root.left
    invert_tree(root.left)
    invert_tree(root.right)

root = TreeNode(1, TreeNode(2), TreeNode(3, TreeNode(5), TreeNode(6)))
invert_tree(root)
print(root.left.val) #3
print(root.left.right.val)#5