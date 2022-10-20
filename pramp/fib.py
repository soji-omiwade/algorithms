def badfib(n: int) -> int:
    if n in (1, 2):
        return 1
    return badfib(n-1) + badfib(n-2)

def fib(n: int) -> int:
    f = [1,1] + [0] * (n-2)
    for i in range(2, n):
        f[i] = f[i-1] + f[i-2]
    return f[n-1]

print(fib(3)) # 2
print(fib(4)) # 3
print(fib(100))

print(badfib(3)) # 2
print(badfib(4)) # 3
print(badfib(100))
