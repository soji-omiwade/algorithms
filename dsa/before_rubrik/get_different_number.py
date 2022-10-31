'''
Given an array arr of unique nonnegative integers, implement a function getDifferentNumber that finds the smallest nonnegative integer that is NOT in the array.
[2, 5, 8] output is zero
set simply.
'''
def get_different_number(arr):
    '''
    can handle duplicates
    '''
    unique_numbers = set()
    for item in arr:
        unique_numbers.add(item)
    maxval = max(arr)
    for i in range(maxval + 1):
        if i not in unique_numbers:
            return i
    return maxval + 1
    
'''
zero index
2, 5, 8, 1
1st 8521
2nd 8521
3rd 8521
4th 8125

2 5 8 1
temp = 2
arr[0] = 8
arr[2] = 2
'''
def get_different_number_noset(arr):
    for idx in range(len(arr)):
        while arr[idx] != idx and arr[idx] < len(arr):
            #swap arr[arr[idx]] with arr[idx]
            temp = arr[idx]
            arr[idx] = arr[arr[idx]]
            arr[temp] = temp
    for i in range(len(arr)):
        if arr[i] != i:
            return i
    return len(arr)

'''can also handle duplicates
set all nums bigger than len(arr) to len(arr)
run counting sort

k in counting sort
2 5 8 1


'''


'''
A
0 1 2 3 4
2 1 0 0 1

C
0 1 2
0 2 5

B
0 1 2 3 4
0 0 1 1 2 

i
0



ci is initially frequency of each element so c[2] = 1, c[1]=2, ...
but becomes number of elements less than or equal to me
=> len(c) == max(A) + 1
'''
def counting_sort(A):
    k = max(A)
    B = len(A) * [None]
    C = [0] * (k + 1)
    for item in A:
        C[item] += 1
    for i in range(1, len(C)):
        C[i] += C[i - 1]
    for i in range(len(A) - 1, -1, -1):
        B[C[A[i]] - 1] = A[i]
        C[A[i]] -= 1
    return B

def get_different_number_counting_sort(arr):
   arr = [min(len(arr), arr[i]) for i in range(len(arr))]
   sorted_arr = counting_sort(arr)
   for i in range(len(arr)):
    if sorted_arr[i] != i:
        return i
    return len(arr)
'''
[0, 1, 2, 3]
ans = 4?
'''
arr = [0, 1, 2, 3]
print(get_different_number(arr))
arr = [2, 5, 8, 1] #ans = 0
print(get_different_number(arr))

get_different_number = get_different_number_noset
arr = [0, 1, 2, 3]
print(get_different_number(arr))
arr = [2, 5, 8, 1] #ans = 0
print(get_different_number(arr))

import random
count = 100
a = [int(count * random.random()) for i in range(count)]
assert sorted(a) == counting_sort(a)
get_different_number = get_different_number_counting_sort 
arr = [0, 1, 2, 3]
print(get_different_number(arr))
arr = [2, 5, 8, 1] #ans = 0
print(get_different_number(arr))
