import sys
"""
1000100011
1100111001
1101000010
"""
k=int(sys.argv[1])
foo=[]
for _ in range(k):
    a=input()
    foo.append([])
    for i in a:
        foo[len(foo)-1].append(int(i))

m=len(foo[0])
count=0
for i in range(k):
    for j in range(m):
        if foo[i][j] \
           and not ((i>0 and foo[i-1][j]) or (j>0 and foo[i][j-1])) \
           and not (j<m-1 and foo[i][j+1] and i>0 and foo[i-1][j+1]):
            print(i,j)
            count += 1
print(count)
            
def show(foo):
    for i in range(len(foo)):
        for j in range(len(foo[0])):
            if j != len(foo[0])-1:
                print(foo[i][j],end=" ")
            else:
                print(foo[i][j])

show(foo)
