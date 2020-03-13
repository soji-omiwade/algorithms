def reverse_diagonals(a):
    m,n=len(a),len(a[0])
    
    first=((i,n-1) for i in range(m-1,-1,-1))
    second=((0,j) for j in range(n-1,-1,-1))
    from itertools import chain
    res=[]
    for r,c in chain(first,second):
        while r<m and 0<c:
            res.append(a[r][c])
            r+=1
            j-=1
    return res

def main():
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