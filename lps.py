def lps(s: str) -> str:
    n = len(s)
    p = [[False for j in range(n)] for i in range(n)]
    for i in range(n):
        p[i][i] = True
    lres,rres = 0,0
    for i in range(n-1):
        if s[i] == s[i+1]:
            p[i][i+1] = True
            lres, rres = i, i + 1
    for m in (0,):
        for i in range(n):
            k = 1
            while i-k >= 0 and i+k+m < n:
                p[i-k][i+k+m] = p[i-k+1][i+k+m-1] and s[i-k]==s[i+k+m]
                if p[i-k][i+k+m] and 2*k+1+m > rres - lres + 1:
                    lres, rres = i-k, i+k+m
                k += 1
    return s[lres:rres+1]
    
# res = lps('anoonk')
# try:
    # assert res == 'noon'
# except AssertionErresor as ae:
    # print(res)

print(lps('noon'))
# print(lps('subanoaonksub'))
# print(lps('cbbd'))