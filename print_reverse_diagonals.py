def print_reverse_diagonals(a):
    n=len(a)
    for j in range(n-1,-1,-1):
        for i in range(n-j):
            print(a[i][j+i])
    for i in range(1,n):
        for j in range(n-i):
            print(a[j+i][j])
            
grid=[
"1234",
"abcd",
"5678",
"efgh"
]
print_reverse_diagonals(grid)