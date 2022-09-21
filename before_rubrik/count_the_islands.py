"""
11110001110 00100010000 00000000010


11110001110 00100010000 00100000010 00100000000

11110001110
00100010000     -> answer = 4 islands
00100000010
00100000000



11110001110 00100010000 00000000010 00100000000

11110001110
00100010000     -> answer = 5 islands
00000000010
00100000000
"""
import sys
def inputt():
    s= input().replace(" ", "")
    l,w = int(sys.argv[1]), int(sys.argv[2])
    return [[int(s[r*w + c]) for c in range(w)] for r in range(l)], l, w
    
def foo(a, l, w):
    """a[i][j] = 0/1 for each i/j"""
    count = 0
    for r in range(l):
        for c in range(w):
            if a[r][c] == 1:
                if (c==0 or a[r][c-1] == 0) and (r==0 or a[r-1][c] == 0):
                    count += 1
    return count
    
if __name__ == "__main__":
    a, l, w = inputt()
    print(l, w, a)
    print(foo(a, l, w))