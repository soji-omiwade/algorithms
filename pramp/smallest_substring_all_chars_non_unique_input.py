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
  
  a:2 b:3 c:2
  track = 0
  needarr = 
  need = len()
  '''
  
  arr = Counter(arr) # {'a': 2, 'b': 3}
  bestleft = -float('inf')
  bestright = float('inf')
  left = 0
  count = Counter()
  track = 0
  for right in range(len(string)):
    if string[right] in arr:
      count[string[right]] += 1
      if count[string[right]] == arr[string[right]]:
        track += 1
    while track == len(arr):
      if right - left < bestright - bestleft:
        bestleft, bestright = left, right
      if string[left] in arr:  
        count[string[left]] -= 1
        if count[string[left]] == arr[string[left]] - 1:
          track -= 1
      left += 1
  if bestleft == - float('inf'):
    return ""
  return string[bestleft:bestright+1] #, bestleft, bestright

arr = ['x','y','z']
string = "xyyzyzyx"
print(get_shortest_unique_substring(arr, string))

arr = ['x','y','z', 'a']
string = "xyyzyazyx"
print(get_shortest_unique_substring(arr, string))


arr = ['x','y', 'y', 'z']
string = "xyyzyzyx"
print(get_shortest_unique_substring(arr, string)) #xyyz

arr = ['x','y','z', 'a']
string = "xyyzyazyx"
print(get_shortest_unique_substring(arr, string))



