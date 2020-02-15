from builtins import pow as bpow

def pow(a, b):
    if b==0:
        return 1
    if b==1:
        return a
    if b<0:
        return 1/pow(a,-b)
    return a*pow(a,b-1)
    
assert pow(2,3) == 8
assert pow(-2,3) == -8
assert pow(5,-4) == bpow(5,-4)

mem={}
def fpow(a,b):
    try:
        res=mem[a,b]
    except:
        if   b==0:   res=1
        elif b==1:   res=a
        elif b<0:    res=1/fpow(a,-b)
        else:        res=fpow(a,b//2)*mem[a,b//2]*fpow(a,b%2)
        mem[a,b]=res
    return res
assert fpow(2,3) == 8
assert fpow(-2,3) == -8
assert fpow(5,-4) == bpow(5,-4)