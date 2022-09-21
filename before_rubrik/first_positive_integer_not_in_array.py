# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

'''
1 2 3 -> 4
i in [1, 3]

1 1 3 -> 2
distinct = {1, 3}
i in [1, 3]

'''
def solution(A):
    distinct = set(A)
    for i in range(1, 1 + len(A)):
        if i not in distinct:
            return i
    else:
        return 1 + len(A)
        
'''
0 1 2 3 5 6
1 3 6 4 1 2
        i
a[5]        

simple
1 2 3

less simple
1 3 2
'''
def solution(A):
    for i in range(len(A)):
        while A[i] != i+1 and 1 <= A[i] <= len(A) and A[A[i] - 1] != A[i]:
            temp = A[i] #3
            A[i] = A[A[i] - 1] # A[1] = A[3 - 1]
            A[temp - 1] =  temp # A[3 - 1]
    for i, el in enumerate(A):
        if i + 1 != el:
            return i + 1
    else:
        return len(A) + 1

