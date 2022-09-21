"""
public double pow(double a, int b) {
    // implementation here
}
"""

def pow(a:float, b:int)->float:
    """
    complexity: T(n) = const + T(n-1) -> O(n)
    """
    if b < 0: return 1/pow(a,-b)
    if b == 0: return 1
    if b == 1: return a
    return a * pow(a,b-1)

def fpow(a:float, b:int, foo=None)->float:
    b = int(b)
    """
    complexity: T(n) = const + T(n)/2,  -> O(lg n)
    """
    if foo is None:
        foo = {}
        foo[a,1] = a
        
    if b < 0: return 1/pow(a,-b)
    if b == 0: return 1
    if b == 1: return a

    try:
        return foo[a,b]
    except Exception:
        res = fpow(a,b//2,foo) * foo[a,b//2]
        if b%2 == 0:
            foo[a,b] = res
        if b%2 == 1:
            res *= a
            foo[a,b] = res
        return res

from math import isclose
assert isclose(pow(1.3,2), 1.69, abs_tol= 1e-8)
assert pow(5,2) == 25
assert pow(25,-2) == 1/625

assert isclose(fpow(1.3,2), 1.69, abs_tol= 1e-8)
assert fpow(5,2) == 25
assert fpow(25,-2) == 1/625
from builtins import pow as bpow
assert fpow(123,45) == bpow(123,45) == pow(123,45)