'''
arr = [ 'p', 'e', 'r', 'f', 'e', 'c', 't', '  ',
                'm', 'a', 'k', 'e', 's', '  ',
                'p', 'r', 'a', 'c', 't', 'i', 'c', 'e']

                start_cur                           curr

swap(arr, output_arr, pi, ti, ppi, ei)
'''
def reverse_words(arr):
  def reverse(lo, hi):
    while lo < hi:
      arr[lo], arr[hi] = arr[hi], arr[lo]
      lo += 1
      hi -= 1
  reverse(0, len(arr) - 1)
  curr = 0
  while curr < len(arr):
    start_curr = curr
    while curr < len(arr) and arr[curr] != ' ':
      curr += 1
    reverse(start_curr, curr - 1)
    curr += 1
  return arr

print(reverse_words(['a']
))
