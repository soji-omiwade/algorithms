def foo(pattern, text):
    if text == "" and pattern =="":
        return 0
    for i in range(len(text)):
        for j in range(len(pattern)):
            if pattern[j] != text[i+j]:
                break
        else:
            return i
    return -1
    
import sys
print(foo(sys.argv[1],sys.argv[2]))


def rk(pattern,text):
    m,n=len(pattern),len(text)
    d=128
    h=pow(d,m-1)
    p=t=0
    for chp,cht in zip(pattern,text):
        p=d*p+ord(chp)
        t=d*t+ord(cht)

    for s in range(n-m+1):
        if p==t:
            return s
        #if below is just to prevent the last case
        #of n-m from executing
        if s+m<=n-1:
            t=(t-ord(text[s])*h)*d+ord(text[s+m])
    return -1
    
print(rk(sys.argv[1],sys.argv[2]))