count_bfind=0
count_hopfind=0
def log_search_without_size(a,k,i=0):
    global count_hopfind
    def bfind(a,k,p,r):
        global count_bfind
        print("\tbfind p r", p, r)
        count_bfind+=1
        if p>r: return -1
        q=(p+r)//2
        if a[q]==k: return q
        
        if k>a[q]: return bfind(a,k,q+1,r)
        if k<a[q]: return bfind(a,k,p,q-1)
        
    count_hopfind+=1
    print('hop i', i)
    if i<len(a):
        if a[0]==k: 
            return 0
        if i==0: 
            i+=1
        if a[i]==k: 
            return i
        if k<a[i]: 
            return bfind(a,k,i//2+1, i-1)
            
        if k>a[i]: 
            return log_search_without_size(a,k,2*i)
    return bfind(a,k,i//2+1,len(a)-1)
    
from random import shuffle
a=[i for i in range(42, 5000 ,70)]
print("ans:",log_search_without_size(a,413))
print()
print("ans:",log_search_without_size(a,462))