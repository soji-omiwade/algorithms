def go(needle, haystack):
    needle = str(needle)
    haystack = str(haystack)
    asc_base = 256
    x = y = 0
    res = []
    m,n = len(haystack), len(needle)
    
    if not needle or n > m: 
        return []
    
    for i, (chn,chh) in enumerate(zip(needle,haystack)):
        x += ord(chn) * asc_base ** i
        y += ord(chh) * asc_base ** i
        
    if x == y: 
        res.append(0)
        
    for i in range(1,m-n+1):
        y -= ord(haystack[i])
        y //= asc_base
        y += ord(haystack[n+i-1]) * asc_base ** (n-1)
        if x == y:
            res.append(i)

    return res
    
print(go("aaa", ""))