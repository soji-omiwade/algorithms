def longest_substring_no_repeats(string):
    '''word: preserved
    
    while move hi out
        ensure low hi is valid (adjust low until so)
        update lo*,hi* based on lo, hi
    '''
    lo = 0
    setsub = set()
    reslo = reshi = 0
    for hi in range(len(string)):
        while string[hi] in setsub:
            setsub.remove(string[lo])
            lo += 1
        setsub.add(string[hi])
        if hi - lo > reshi - reslo:
            reslo, reshi = lo, hi
    return reslo, reshi
            
string = 'preserved'
print(longest_substring_no_repeats(string))
assert longest_substring_no_repeats(string) == (0, 3)
string = 'paypalishiring'
assert longest_substring_no_repeats(string) == (2, 8)
