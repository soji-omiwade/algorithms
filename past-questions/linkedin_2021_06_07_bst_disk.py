'''
    Question # 2:
    
    
    Design an algorithm and write code to serialize and deserialize a binary tree. Writing the tree to a file is called ‘serialization’ and reading back from the file to reconstruct the exact same binary tree is ‘deserialization’. Assume that every node has an integer value.
        
    

            
    a     1
 b     c    2
n  n  n   d   4
a, b, c, n, n, n, d  8 

from collections import deque
nodes = deque([root])
count = 1
while nodes:
    for i in range(count):
        
        node = nodes.popleft()
        if not node:
            write(None)
        else:
            write(node.val)
            nodes.append(node.left)
            nodes.append(node.right)
    count = count * 2

    
    public class BinaryTree {
 
    private Node root;
 
    private static class Node {
        int data;
        Node left;
        Node right;
    }
 
    /**
     * Write the serialized form of this tree into the given stream.
     */
    public void serialize(OutputStream into) throws IOException {
        // implement this
    }
 
    /**
     * Reconstruct a tree from its serialized form.
     */
    public static BinaryTree deserialize(InputStream from) {
        // implement this
    }
}
'''