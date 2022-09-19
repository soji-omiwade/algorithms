from collections import Counter
def get_shortest_unique_substring(arr, string):
  '''
  input:  
  arr = ['x','y','z']
  str = "xyyzyzyx"
         ^  ^
  grow the string to the right,
  once all chars required are collected, then from left shrink the string until 
  some char is missing, always updating the optimal endpoints, bestleft, bestright
  '''
  arr = set(arr)
  bestleft = -float('inf')
  bestright = float('inf')
  left = 0
  count = Counter()
  for right in range(len(string)):
    if string[right] in arr:
      count[string[right]] += 1
    while len(count) == len(arr):
      if right - left < bestright - bestleft:
        bestleft, bestright = left, right
      if string[left] in arr:  
        count[string[left]] -= 1
        if count[string[left]] == 0:
          del count[string[left]]
      left += 1
  if bestleft == - float('inf'):
    return ""
  return string[bestleft:bestright+1] #, bestleft, bestright

arr = ['x','y','z']
string = "xyyzyzyx"
print(get_shortest_unique_substring(arr, string))
