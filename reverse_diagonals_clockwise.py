def reverse_diagonals(a):
    res=[]
    m,n=len(a),len(a[0])
    for j in range(n):
        for k in range(j+1):
            res.append(a[k][j-k])
    for i in range(1,m):
        for k in range(m-i):
            res.append(a[i+k][n-1-k])
    return res
            
a=[
[1,2,3],
[4,5,6],
[7,8,9],
]
assert reverse_diagonals(a) == [1,2,4,3,5,7,6,8,9]