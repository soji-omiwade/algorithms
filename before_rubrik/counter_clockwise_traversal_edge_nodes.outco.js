
let tree =
{
"value": "a",
"left": {
"value": "g",
"left": {
"value": "m",
"left": {
"value": "f",
"left": null,
"right": null
},
"right": {
"value": "c",
"left": null,
"right": null
}
},
"right": {
"value": "p",
"left": {
"value": "s",
"left": null,
"right": null
},
"right": {
"value": "r",
"left": null,
"right": null
}
}
},
"right": {
"value": "w",
"left": {
"value": "u",
"left": {
"value": "t",
"left": null,
"right": null
},
"right": {
"value": "o",
"left": null,
"right": null
}
},
"right": {
"value": "z",
"left": {
"value": "k",
"left": null,
"right": null
},
"right": {
"value": "x",
"left": null,
"right": null
}
}
}
}
/*

For this task, you will be given the elements of a perfect binary tree of characters,
 stored within a simple tree data structure.

Your goal is to write a function that starts at the root of the tree and 
returns a counter clockwise traversal of the nodes at the edge of the tree.

1. understand 
- I/o
-constrains 

2. Diagram 
- 
3. pseudo code 
4. code 

input: 
            a
           /   \
         g       w
        / \     / \
       m   p   u    z
      / \ / \ / \  / \
     f  c s r t  o k  x
     
Output: 
[a, g, m, f c s r t  o k  x,z, w ]

  a 
 / \
d   b

[a, d, b]


constrains: 
- edge of the tree
- perfect binary tree : A perfect binary tree is a tree where every non-leaf node has exactly two children,
 and all leaf nodes are at the same level
- characters of lower case 


-------
BFS 
DFS 
recurse 

left 
add the value to the result |action
go to the next node | traverse 



children 
add the value to the result | action 
go to the next node | traverse 



right 
go to the next node | traverse 
add the value to the result |action



 */
 
 function left(cur, res){
   //base 
   if(!cur.left){
     return res;
   }
   
   res.push(cur.value)
   return left(cur.left, res)
 }
 
 function children(cur, res){
   //base case 
   if(!cur.left){
     res.push(cur.value)
     return res
   }
   //traverse 
   children(cur.left, res)
   children(cur.right, res)
   return res
 }
 
 function right(cur, res){
   //base case 
   if(!cur.right){
     return res
   }
   
   //traverse 
   right(cur.right, res)
   res.push(cur.value)
   return res
 }
 
 function counterClockwiseTraversal(tree){
  //  let result = [tree.value]
  //  result.push(...left(tree.left, []))
  //  result.push(...children(tree, []))
  //  result.push(...right(tree.right, []))
  let result = []

  function traverse(cur, leftMost, rightMost){
    //base case 
    //left
    if(leftMost && cur.left){
      result.push(cur.value)
    }
    //leaves 
    if(!cur.left){
      result.push(cur.value )
      return 
    }
    //traverse 
     traverse(cur.left, leftMost, false)
      traverse(cur.right, false, rightMost)
    //right
    if(rightMost && !leftMost){
      result.push(cur.value)
    }
  }  
   
   traverse(tree, true, true)
   return result
 }
 
 console.log(counterClockwiseTraversal(tree))








