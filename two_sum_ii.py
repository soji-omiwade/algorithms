def two_sum(a,target):
    b=list(a)
    for i in range(len(b)):
        b[i]=(b[i],i)
    i,j=0,len(a)-1
    while i<j:
        sum=b[i][0]+b[j][0]
        if sum == target:
            return [b[i][1]] + [b[j][1]]
            i+=1
            j-=1
        elif sum < target:
            i+=1
        else:
            j-=1
    return []

from random import shuffle
a=[1,2,4,3,5,6,7,8,9,10]
# shuffle(a)
assert two_sum(a,6)==[0,4]

a=[1,2,3,4,3,5,6,7,8,9,10]
# shuffle(a)
assert two_sum(a,6)==[0,5]

assert two_sum([],42)==[]