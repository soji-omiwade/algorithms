'''
[1,2,3,4]; target = 10
function 4sum(target)
  #DON'T NEED because it's not like we say bidx > cidx  if len(arr) is less than four, return empty array

  #need a + b + c + d = target
  #solve 3sum against target - d
  for didx,d in arr
    a,b,c =  3sum(arr, target - d, didx)
      if a is not null
        return a,b,cd
  return []
  

function 3sum(target, didx)
  #find a + b + c = target  
  for cidx in range(arr), cidx not equal to didx
     aidx, bidx = 2sum(target - c, cidx, didx)
     if aidx is not nil
        return a, b, c
  return null, null, null
        
function 2sum(target, cidx, didx)
  found = set()
  for aidx,firstnum in range(arr) 
    if target - firstnum in found and idx[target-firstnum] not in (cidx, didx)
      return (aidx, bidx)
      add firstnum to set
    return None, None
'''
def find_array_quadruplet(arr, s):
    # [1,2,3,4]; target = 10
    def four_sum(target):
        #DON'T NEED because it's not like we say bidx > cidx  if len(arr) is less than four, return empty array
        #need a + b + c + d = target
        #solve 3sum against target - d
        for didx,d in enumerate(arr):
            a,b,c =  three_sum(target - d, didx)
            if a is not None:
                return a, b, c, d
        return []
      

    def three_sum(target, didx):
        #find a + b + c = target  
        for cidx, c in enumerate(arr):
            if cidx != didx:
                a, b = two_sum(target - c, cidx, didx)
                if a is not None:
                    return a, b, c
        return None, None, None
            
    def two_sum(target, cidx, didx):
        aidxlookup = {}
        for aidx, firstnum in enumerate(arr):
            if aidx not in (cidx, didx):
                if (target - firstnum in aidxlookup
                and aidxlookup[target - firstnum] not in (cidx, didx)):
                    return (firstnum, target - firstnum)
                aidxlookup[firstnum] = aidx
        return None, None

    return sorted(four_sum(s))

arr = [1,9,0,2,6,3,4]
s = 10
print(find_array_quadruplet(arr, s))