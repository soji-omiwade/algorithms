'''
Given an array arr of unique nonnegative integers, implement a function getDifferentNumber that finds the smallest nonnegative integer that is NOT in the array.
[2, 5, 8] output is zero
set simply.
'''
def get_different_number(arr):
    '''
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
[0, 1, 2, 3]
ans = 4?
'''
arr = [0, 1, 2, 3]
print(get_different_number(arr))
arr = [2, 5, 8] #ans = 0
print(get_different_number(arr))
