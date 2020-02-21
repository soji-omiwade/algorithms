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
    for i in range(min(m,n)):
        t=d*t+ord(text[i])
    for chp in pattern:
        p=d*p+ord(chp)
    s=0
    while True:
        if p==t:
            return s
            
        if s+m>n-1:
            break
        t=(t-ord(text[s])*h)*d+ord(text[s+m])
        s+=1
    return -1
    
print(rk(sys.argv[1],sys.argv[2]))