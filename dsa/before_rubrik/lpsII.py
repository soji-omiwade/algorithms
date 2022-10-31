def lpal(s: str) -> str:
    p = []
    lres, rres = 0, 0
    n = len(s)
    for i in range(n):
        p.append([])
        for j in range(n):
            if i == j or (j == i + 1 and s[i] == s[j]):
                p[i].append(True)
                if j > i:
                    lres, rres = i, j
            else:
                p[i].append(False)
    for m in (0, 1):
        for i in range(n):
            k = 1
            while i-k >= 0 and i+k+m < n:
                p[i-k][i+k+m] = p[i-k+1][i+k-1+m] and s[i-k] == s[i+k+m]
                if p[i-k][i+k+m] and 2*k+m > rres-lres:
                    lres, rres = i-k, i+k+m
                k += 1
    return s[lres:rres+1]
    

assert lpal('a') == 'a'
assert lpal('bb') == 'bb'
assert lpal('car') == 'c'
assert lpal('cbbd') == 'bb'

assert lpal('bab') == 'bab'
assert lpal('qrbab') == 'bab'
assert lpal('qrbabst') == 'bab'

assert lpal('stqnoonr') == 'noon'
                