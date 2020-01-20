def count_and_say(n):
    """google count and say"""
    s = "1"
    
    for _ in range(n-1):
        k=0
        t=""
        while k < len(s):
            i = k + 1
            while i < len(s):
                if s[i] != s[k]:
                    break
                i+=1
            t += str(i - k) + s[k]
            k += (i-k)
        s = t
        
    return(s)