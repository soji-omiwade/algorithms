def atoi(s):
    res = 0
    for i in range(n):
        res = 10*res + ord(s[i]) - ord("0")
    return res
assert atoi("42") == 42
assert atoi("0") == 0
assert atoi("4278") == 4278
int_max = (2**32)-1
assert atoi(str(int_max)) == int_max
assert atoi(str(int_max+1)) == int_max
