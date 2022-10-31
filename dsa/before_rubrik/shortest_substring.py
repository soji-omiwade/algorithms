from collections import Counter
def go(s: str, sub: str) -> str:
    if len(s) * len(sub) == 0:
        return ""
    i = 0
    im = 0
    jm = len(s)
    sub_set = set(sub) 
    lettercount = Counter()
    for j in range(len(s)):
        if s[j] in sub_set:
            lettercount[s[j]] += 1
        while len(lettercount) == len(sub_set):
            if j-i < jm-im:
                im, jm = i, j
            if s[i] in sub_set:
                lettercount[s[i]] -= 1
                if lettercount[s[i]] == 0:
                    del lettercount[s[i]]
            i += 1
    return s[im:jm+1]
assert go("abracadabra", "abc") == "brac"
assert go("abracadabra", "adc") == "cad"
assert go("", "jk") == ""
assert go("abc", "") == ""
assert go("", "") == ""
