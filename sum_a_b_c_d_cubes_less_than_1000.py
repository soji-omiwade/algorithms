"""
find all a,b,c,d  such that sum(a3,b3,c3,d3) < 1000
"""
n=1000
ncuberoot = 1+int(pow(1000,1/3))
cache = {}
for i in range(ncuberoot):
    cache[i] = i**3
for a in range(n):
    for b in range(a,n):
        for c in range(b,n):
            for d in range(c,n):
                sum = cache[a] + cache[b] + cache[c] + cache[d]
                if sum < n:
                    print(a,b,c,d, sum)
                else:
                    break
