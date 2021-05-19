from collections import Counter
def go(s: str, substr: str) -> str:
    if not s:
        return None
    if not substr:
        return ""
    i = 0
    im = 0
    jm = len(s)        
    count = 0
    target = Counter(substr)
    current = Counter()
    for j in range(len(s)):
        if s[j] in target:
            current[s[j]] += 1
            if current[s[j]] == target[s[j]]:
                count += 1
                while count == len(target):
                    if j-i < jm-im:
                        im, jm = i, j
                    if s[i] in target:
                        if current[s[i]] == target[s[i]]: 
                            count -= 1
                        current[s[i]] -= 1
                    i += 1
    return s[im:jm+1]
assert go("ABRACADABRA", "ABAC") == "ABRAC"
assert go("ABRACADABRA", "ADAC") == "ACAD"
assert go("", "abc") is None
assert go("abc", "") == ""
assert go("", "") is None