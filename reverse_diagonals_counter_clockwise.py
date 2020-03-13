def reverse_diagonals(a):
    m,n=len(a),len(a[0])
    res=[]
    for i in range(m-1,-1,-1):
        for k in range(m-i):
            res.append(a[k+i][n-1-k])
    for j in range(n-2,-1,-1):
        for k in range(1+j):
            res.append(a[k][j-k])
    return res

a=[
[1,2,3],
[4,5,6],
[7,8,9],
]
assert reverse_diagonals(a) == [9,6,8,3,5,7,2,4,1]
