def print_reverse_diagonals(a):
    res=[]
    m=len(a)
    n=len(a[0])
    for j in range(n-1,-1,-1):
        for i in range(min(m,n-j)):
            res.append(a[i][j+i])
    for i in range(1,m):
        for j in range(min(m-i,n)):
            res.append(a[j+i][j])
    return res        
grid=[
"1234",
"abcd",
"5678",
"efgh",
]
assert print_reverse_diagonals(grid) == list("43d2c81b7ha6g5fe")
grid=[
"1234",
"5678",
]
assert print_reverse_diagonals(grid) == list("43827165")
grid=[
"12",
"34",
"56",
"78",
]
# print(print_reverse_diagonals(grid))
assert print_reverse_diagonals(grid) == list("21436587")