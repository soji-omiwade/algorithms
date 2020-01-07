"""
example: go(.24, .01) = 1,4
"""
import sys

def make_relatively_prime(left, right):

    p = 2
    while True:
        if p > min(left,right):
            break
        if left % p == 0 and right % p == 0:
            left //= p
            right //= p
            print(left, right)
        else:
            p += 1
        
    return left, right

val, tol = float(sys.argv[1]), float(sys.argv[2])

expon = len(sys.argv[1])-1
right = pow(10,expon)
tol *= right
left = val * right

print(left,right)
print(make_relatively_prime(int(left), int(right)))
