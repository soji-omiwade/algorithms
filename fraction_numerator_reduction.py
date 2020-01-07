import sys
val, tol = float(sys.argv[1]), float(sys.argv[2])

expon=len(sys.argv[1])-1
denom=pow(10,expon)
num=val*denom
tol*=denom

assert(num == int(num))
res=x=y=int(num)
while x <= tol+num:
    if denom % x == 0:
        res,denom = 1,denom//x
        break
    elif denom % y == 0:
        res,denom = 1,denom//y
        break
    x+=1
    y-=1
print(res,denom)

                                 

