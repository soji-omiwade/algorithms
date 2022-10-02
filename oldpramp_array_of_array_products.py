def array_of_array_products(arr):
  #l and r based off of arr
  res = []
  for i in range(-1, n-1):   # for (int i = -1; i < n - 1; i ++ )
    lval = 1
    if i > -1
      lval = l[i]

    rval = 1
    if i != n-2 # 2
     rval = r[i+1]

    res.append(lval*rval)  

  return res



'''
import java.io.*;
import java.util.*;

class Solution {
  static int[] arrayOfArrayProducts(int[] arr) {
    // your code goes here
  }

  public static void main(String[] args) {

  }

}
/*
[2,  4,  3   7]

l   [1 2 24 243]
r   [734 73 7 1]
res [734 2-73 24-7  243]

'''


'''
l: [8 810 8102 ...]
r: [...]

[10246, 8-246 810-46 81024]
[l*  r(-4)]   l0 *  r(-3)    l1 r(-2)   l3 r*
     -n            -n+1       -n+2 
                 
magic [. . . ]

[,    1,   1]
10*2  

'''

