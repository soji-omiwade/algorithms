def shifted_arr_search(shiftArr, num):
  start, end = 0, len(shiftArr)-1
  while start<=end:
    mid = start+(end-start)//2
    if shiftArr[mid] == num:
      return mid
    if shiftArr[mid] >= shiftArr[start]: # the left part of the arr is sorted
        if num >= shiftArr[start] and num< shiftArr[mid]: # arr[start] <= num < arr[mid]
          end = mid-1
        else:
          start = mid+1
    else:
        if num> shiftArr[mid] and num<= shiftArr[end]: # arr[mid] < num <= arr[end]
          start = mid+1
        else:
          end = mid-1 
  return -1
  
assert shifted_arr_search([3,2], 3) == 0
assert shifted_arr_search([3,2], 2) == 1
assert shifted_arr_search([9, 12, 17, 2, 4, 5], 12) == 1
assert shifted_arr_search([9, 12, 17, 2, 4, 5], 2) == 3
assert shifted_arr_search([9, 12, 17, 12, 4, 5], 4) == 4
assert shifted_arr_search([9, 12, 17, 12, 4, 5], 42) == -1
