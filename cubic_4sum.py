"""

4sum: a + b + c + d = target
3sum: b + c + d = target - a
2sum: c + d = target - a - b
find all a,b,c,d  such that sum(a3,b3,c3,d3) < 1000
"""
def foursum(n=1000):
    res = []
    for a in range(n):
        for b in range(a, n):
            # nutarget = n - a**3 - b**3
            #now find x in range [b ... nutarget^(1/3)] where x**3 + hi**3 < nutarget
                #then , wait no need for binsearch. because we want a report!
            for c in range(b, n):
                if lo**3 + hi**3 < nutarget:
                    res.append((a, b, lo, hi))
                    
                elif 
                
res = foursum()
assert len(res) == len(set(res))
print(res, '\n', len(res))