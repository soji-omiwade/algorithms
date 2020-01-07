import sys
m,n,a,b,c,d=int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5]), int(sys.argv[6])

foo=[[0 for j in range(n)] for i in range(m)]

def reset(foo):
    xstep=ystep=1
    if c < a: xstep=-1      
    if d < b: ystep=-1

    foo[a][b]=foo[c][d]=1
    the_max=max(abs(c-a),abs(d-b))

    for i in range(the_max-1):
        xval=a
        if a < c:
            xval = min(a+xstep,c)
            xstep+=1
        elif a > c:
            xval=max(a+xstep,c)
            xstep-=1

        yval=b
        if b < d:
            yval = min(b+ystep,d)
            ystep+=1
        elif b > d:
            yval=max(b+ystep,d)
            ystep-=1
        foo[xval][yval] = 1



def show(foo):
    m,n=len(foo), len(foo[0])
    for i in range(m):
        for j in range(n):
            print(f"{foo[i][j]} ",end="")
        print("")

show(foo)
reset(foo)
print()
show(foo)
