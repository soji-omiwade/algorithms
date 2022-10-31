def reverse_words(arr):
  def get_spaceloc_from_nonspaceloc(sloc):
    while sloc < len(arr) and arr[sloc] != ' ':
      sloc += 1
    return sloc
  
  def get_nonspaceloc_from_spaceloc(sloc):
    while sloc < len(arr) and arr[sloc] == ' ':
      sloc += 1
    return sloc
  
  def reverse(lo, hi):
    while lo <= hi:
      arr[lo], arr[hi] = arr[hi], arr[lo]
      lo += 1
      hi -= 1
      
  arr.reverse()
  lo = get_nonspaceloc_from_spaceloc(0)
  while lo < len(arr):
    hi = get_spaceloc_from_nonspaceloc(lo) - 1
    reverse(lo, hi)
    lo = get_nonspaceloc_from_spaceloc(hi + 1) 
  return arr

arr = [ ' ', ' ', 'p', 'e', 'r', 'f', 'e', 'c', 't', '  ',
        'm', 'a', 'k', 'e', 's', '  ',
        'p', 'r', 'a', 'c', 't', 'i', 'c', 'e' ]

print(reverse_words(arr))
'''
output: [ 'p', 'r', 'a', 'c', 't', 'i', 'c', 'e', '  ',
          'm', 'a', 'k', 'e', 's', '  ',
          'p', 'e', 'r', 'f', 'e', 'c', 't' ]
'''
