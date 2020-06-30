def foo(a, b):
    c = a + b
    return c

def coo(a, b):
    c = a * b * foo(a, b)
    c+=1
    c*=2
    while a > 0:
        a-=1
    a += 3
    c += foo(a,b)
    return c

if __name__ == "__main__":
    coo(2, 3) + foo(5,8) + coo(1,1)
    print("all done")