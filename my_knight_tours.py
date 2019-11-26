import sys
# w,h: width -> columns; height -> rows
h,w=int(sys.argv[1]), int(sys.argv[2])
moves = [(1,2),(1,-2),(-1,2),(-1,-2),(2,1),(2,-1),(-2,1),(-2,-1)]
a = [[False for _ in range(w)] for _ in range(h)]
a[0][0] = True
count = 1
def foo(x=0,y=0):
    global count
    for (dx,dy) in moves:
        if 0 <= x+dx < w and 0 <= y+dy < h and not a[y+dy][x+dx]:
            a[y+dy][x+dx] = True
            foo(x+dx,y+dy)
            count += 1
            break
    
 
def go():
    foo()
    for i in range(h):
        for j in range(w):
            if a[i][j] == False:
                return False
    return True
    
go()
# if not go(): count = 0
print(count)
print(a)
