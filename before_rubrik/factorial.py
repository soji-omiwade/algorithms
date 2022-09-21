"""
This is the "example" module

The example module supplies one function, factorial(). For example, 

>>> factorial(5)
120
"""

def factorial(n):
    """Return the factorial of n, an exact integer >= 0

    >>> [factorial(n) for n in range(6)]
    [1, 1, 2, 6, 24, 120]
    >>> factorial(30)
    265252859812191058636308480000000
    >>> factorial(-1)
    Traceback (most recent call last):
        ...
    ValueError: n must be >= 0

    Factorials of floats are OK, but the float must be an exact integer:
    >>> factorial(30.1)
    Traceback (most recent call last):
        ...
    ValueError: n must be exact integer
    >>> factorial(30)
    265252859812191058636308480000000

    It must also not be ridiculously large:
    >>> factorial(1e100)
    Traceback (most recent call last):
        ...
    OverflowError: n too large
    """
    import math

    try: 
        assert math.floor(n) == n
    except AssertionError:
        raise ValueError("n must be exact integer")
    try:
        assert n >= 0
    except AssertionError: 
        raise ValueError("n must be >= 0")
    try: 
        assert n+1 != n
    except AssertionError:
        raise OverflowError("n too large")
        
    if n == 0: 
        return 1
    else:
        return n * factorial(n-1)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    
    