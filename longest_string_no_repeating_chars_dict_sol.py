def longest_substring_norepeats(string):
    '''prese    rved
       l   h
        while hi < len
            validate lo...hi will be ok.
                -> if string[hi] dictsub[hi] in 
            update reslo, reshi
    '''
    dictsub = {}
    reslo = reshi = lo = 0
    
    for hi in range(len(string)): # 5
        if string[hi] in dictsub:
            lo = max(lo, dictsub[string[hi]] + 1) #2
        dictsub[string[hi]] = hi # d = {p: 0, r: 1, e: 4, s: 3}
        if hi - lo > reshi - reslo:  
            reshi, reslo = hi, lo   #3, 0
    return reslo, reshi
    
string = 'preserved'
print(longest_substring_norepeats(string))
assert longest_substring_norepeats(string) == (0, 3)
string = 'paypalishiring'
assert longest_substring_norepeats(string) == (2, 8)
