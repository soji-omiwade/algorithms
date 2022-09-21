def count_them(a, b):
    if b == 0: return 0
    return a//b + count_them(b, a%b)

def i_count_them(a, b):
    count = 0
    while  True:
        count += a // b
        a,b = b,a % b
        if b == 0:
            break
    return count