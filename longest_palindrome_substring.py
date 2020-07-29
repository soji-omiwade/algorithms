def lonpalsub(s: str) -> str:
    n = len(s)
    resl =  resr = 0
    for m in (0,1):
        for i in range(n):
            k = 0
            while 0 <= i-k and i+k+m < n and s[i-k] == s[i+k+m]:
                if 2*k+m > resr - resl:
                    resl, resr = i-k, i+k+m
                k += 1
    return s[resl:resr + 1]
    
assert lonpalsub('anonk') == 'non'
assert lonpalsub('anoonkrasnon') == 'noon'
assert lonpalsub('abcdef') == 'a'
assert lonpalsub('anoonkrasnooooon') == 'nooooon'

