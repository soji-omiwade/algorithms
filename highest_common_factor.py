def hcf(a):
    def keep_going(a, p):
        for x in a:
            if x % p != 0:
                return False
        return True
    def next_prime(p):
        def is_prime(p):
            for x in range(2,p):
                if p%x == 0:
                    return False
            return True
        if p == 2:
            return 3
        while True:
            p += 2
            if is_prime(p):
                return p
        
    p = 2
    hcf = 1
    while p <= min(a):
        while keep_going(a,p):
            for i in range(len(a)):
                a[i] //= p
            hcf *= p
        p = next_prime(p)
    return hcf
    
import sys
if __name__ == "__main__":
    print(hcf([int(sys.argv[i]) for i in range(1, len(sys.argv))]))
    
    