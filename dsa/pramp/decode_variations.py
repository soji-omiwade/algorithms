def decodeVariations(s: str) -> int:
    def validate(lo, hi):
        if lo == -1:
            return True
        return 1 <= int(s[lo:hi+1]) <= 26

    def decode(lo, hi, tracker, res):
        if lo == n:
            ress.append(list(res))
            return bool(tracker)
        
        count = 0
        res.append(s[lo:hi+1])
        for nexthi in range(hi+1, n):
            count += decode(hi+1, nexthi, tracker and validate(lo, hi), res)
        res.pop()
        return count

    n = len(s)
    ress = []
    res = []
    print(ress)
    return decode(-1, -1, True, [])
s = "1267"
print(decodeVariations(s))
'''
1 2 6 7
1 26 7
12 6 7
ans = 3
'''

'''
1262

                .
1     2      6      2

1: 2, 6, 2
1: 
'''
  
'''
def decodeVariations(S):
  """
  @param S: str
  @return: int
  """
  def helper(curridx=0, oneres=None, tracker=True):
    if oneres is None:
      oneres = []
    count = 0
    for endidx in range(curridx, n):
      cand = S[curridx:endidx+1]
      tracker = tracker and 1 <= int(cand) <= 26
      oneres.append(cand)
      count += helper(endidx + 1, oneres, tracker)
      oneres.pop()
    if curridx == n:
      results.append(list(oneres))
      count = int(tracker)
    return count
  
  n = len(S)
  results = []
  count = helper()
  #for result in results: 
  #  print(result)
  #print(count)    
  return count
S = '1262'
print(decodeVariations(S))
'''


'''
1262

                .
1     2      6      2

1: 2, 6, 2
1: 
'''
  
'''
def decodeVariations(S):
  """
      if memo[curridx][endidx] == -1:
        memo[curridx][endidx] = helper(endidx + 1, oneres, tracker)
      else:
        print("using memo ", curridx, endidx)

  @param S: str
  @return: int
  """
  def helper(curridx=0, oneres=None, tracker=True):
    if oneres is None:
      oneres = []
    count = 0
    for endidx in range(curridx, n):
      if True or memo[curridx][endidx] == -1:        
        cand = S[curridx:endidx+1]    
        oneres.append(cand)
        print('before', curridx, endidx, memo[curridx][endidx])
        memo[curridx][endidx] = helper(endidx + 1, oneres, tracker and 1 <= int(cand) <= 26)
        print('after', curridx, endidx, memo[curridx][endidx])
        oneres.pop()
      else:
        print("using memo ", curridx, endidx)
      count += memo[curridx][endidx]
    if curridx == n:
      results.append(list(oneres))
      count = int(tracker)
    return count
  
  n = len(S)
  results = []
  memo = [[-1 for _ in range(n)] for _ in range(n)]
  count = helper()
  for result in results: 
    print(result)
  print(count)    
  return count

S = '1262'
print(decodeVariations(S))
'''

'''
('using memo ', 3, 3)
('using memo ', 2, 2)
('using memo ', 2, 3)
('using memo ', 3, 3)

['1', '2', '6', '2']
['1', '2', '62']
['1', '262']
['1262']

4
'''
