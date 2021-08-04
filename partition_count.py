'''
babaa
'''
from typing import List, Tuple
def acount(start, end):
    count = 0
    for i in range(start, end):
        if s[i] == "a":
            count += 1
    return count
    
def solution(s) -> Tuple[int, List[str]]:
    '''
    n = 5
    0 1 234
    b|a|baa
    '''
    def generate_acount():
        '''
        aabcde
        '''
        acount = [[0 for j in range(n)] for i in range(n)]
        for i in range(n):
            acount[i][i] = 1 if s[i] == a else 0
        for i in range(n):
            for j in 
    n = len(s)
    acount = generate_acount()
    count = 0
    for midx in range(1, n - 1):
        for ridx in range(2, n):
            leftcount = acount[0][midx - 1]
            midcount = acount[midx][ridx - 1]
            rightcount = acount[ridx][n - 1]
            if leftcount == midcount == rightcount:
                count += 1
    return count
    '''
    
def solution(s) -> Tuple[int, List[str]]:
    '''
    i = 1
    j = 2
    0 1 2 3 4
    b|aba|a
    n = 5
    '''
    n = len(s)
    if acount(0, n) % 3 != 0:
        return 0, []
    count = 0
    lis = []
    for i in range(1, n - 1):
        for j in range(i + 1, n):
            left = acount(0, i)
            mid = acount(i, j)
            right = acount(j, n)
            if left == mid == right:
                count += 1
                lis.append((i,j))
    return count, lis
    
s = "babaa"
print(s, solution(s))
s = "ababa"
print(s, solution(s))
s = "aba"
print(s, solution(s))
s = "bbbbb"
print(s, solution(s))

