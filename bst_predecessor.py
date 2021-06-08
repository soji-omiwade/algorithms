#########################################################
# CODE INSTRUCTIONS:                                    #
# 1) The method findInOrderSuccessor you're asked      #
#    to implement is located at line 30.                #
# 2) Use the helper code below to implement it.         #
# 3) In a nutshell, the helper code allows you to       #
#    to build a Binary Search Tree.                     #
# 4) Jump to line 88 to see an example for how the      #
#    helper code is used to test findInOrderSuccessor.  #
#########################################################


# A node 
class Node:

  # Constructor to create a new node
  def __init__(self, key):
    self.key = key 
    self.left = None
    self.right = None
    self.parent = None

# A binary search tree 
class BinarySearchTree:

  # Constructor to create a new BST
  def __init__(self):
    self.root = None

  def find_in_order_predecessor(self, inputNode):
    def get_parent_finder():
        def binsearch(node):
            if node is inputNode:
                return
            if node.key > inputNode.key:
                #go to the left; but save that node's parent as node first
                #note there has to be a left node if the inputNode exists
                parent_finder[node.left] = node
                binsearch(node.left)
            else:
                parent_finder[node.right] = node
                binsearch(node.right)
                
        parent_finder = {self.root: None}
        binsearch(self.root)
        return parent_finder
        
    def parent_helper(node):
        #have to find the parent that is smaller than inputNode. 
        if not node:
            return None
        if node.key < inputNode.key:
            return node
        return parent_helper(node.parent)
        
    def right_helper(node):
        if not node.right:
            return node
        return right_helper(node.right)
        
    parent_finder = get_parent_finder()
    if inputNode.left:
        return right_helper(inputNode.left)
    return parent_helper(parent_finder[inputNode])

  # Given a binary search tree and a number, inserts a
  # new node with the given number in the correct place
  # in the tree. Returns the new root pointer which the
  # caller should then use(the standard trick to avoid 
  # using reference parameters)
  def insert(self, key):
    def insert_helper(node):
        if insert_node.key < node.key:
            if node.left:
                insert_helper(node.left)
            else:
                node.left = insert_node
        else:
            if node.right:
                insert_helper(node.right)
            else:
                node.right = insert_node
            
    insert_node = Node(key)
    if not self.root:
        self.root = insert_node
        return
    insert_helper(self.root)
    
  def print_tree(self, node):
    if not node:
        return
    self.print_tree(node.left)
    print(node.key, end=", ")
    self.print_tree(node.right)

  # Return a reference to a node in the BST by its key.
  # Use this method when you need a node to test your
  # findInOrderSuccessor function on
  def getNodeByKey(self, key):
    
    currentNode = self.root
    while(currentNode is not None):
      if(key == currentNode.key):
        return currentNode
        
      if(key < currentNode.key):
        currentNode = currentNode.left
      else:
        currentNode = currentNode.right
        
    return None
        
######################################### 
# Driver program to test above function #
#########################################

# Create a Binary Search Tree
bst  = BinarySearchTree()
bst.insert(20)
bst.insert(9);
bst.insert(25);
bst.insert(5);
bst.insert(12);
bst.insert(11);  
bst.insert(14);    

import sys

# Get a reference to the node whose key is 9
test = bst.getNodeByKey(int(sys.argv[1]))

bst.print_tree(bst.root)
print()
# Find the in order successor of test
succ = bst.find_in_order_predecessor(test)

# Print the key of the successor node
if succ is not None:
    print ("\nInorder Successor of %d is %d " \
            %(test.key , succ.key))
else:
    print ("\nInorder Successor doesn't exist")
