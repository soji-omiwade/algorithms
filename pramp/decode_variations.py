'''
1262

                .
1     2      6      2

1: 2, 6, 2
1: 
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
  '''
  for result in results: 
    print(result)
  print(count)    
  '''
  return count
S = '1262'
print(decodeVariations(S))
