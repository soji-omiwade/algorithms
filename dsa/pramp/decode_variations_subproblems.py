def decodeVariations(s):
    def validate(lo, hi): 
        return 1 <= int(s[lo:hi+1]) <= 26

    def decode(lo, hi, res):
        if hi == n - 1:
          count = 1
          ress.append(list(res))
        else:
          count = 0
          for nhi in range(hi + 1, n):
              res.append(s[hi+1:nhi+1])
              count += decode(hi + 1, nhi, res)
              res.pop()
        return int(validate(lo, hi)) * count
    memo = {}
    n = len(s)
    ress = []
    res = []
    count = 0
    for hi in range(n):
        res.append(s[:hi+1])
        count += decode(0, hi, res)
        res.pop()
    #print(ress)
    return count

S = '1262'
print(decodeVariations(S))
