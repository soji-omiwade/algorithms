from typing import List
def get_reverse_diagonals(a: List[List[int]]):
    res = []
    m,n=len(a),len(a[0])
    for i in range(m-1,-1,-1):
        for k in range(min(n,m-i)):
            res.append(a[i+k][n-1-k])
    for j in range(n-2,-1,-1):
        for k in range(min(m,j+1)):
            res.append(a[k][j-k])
    return res
grid = [
[1,2,3],
[4,5,6],
[7,8,9],
]
res=[9,6,8,3,5,7,2,4,1]
print(get_reverse_diagonals(grid))
assert get_reverse_diagonals(grid) == res
grid = [
[1,2,3],
[4,5,6],
]
res = [6,3,5,2,4,1]
assert get_reverse_diagonals(grid) == res
grid = [
[ 1, 2, 3],
[ 4, 5, 6],
[ 7, 8, 9],
[10,11,12],
[13,14,15],
]
res = [15,12,14,9,11,13,6,8,10,3,5,7,2,4,1]
assert get_reverse_diagonals(grid) == res
    