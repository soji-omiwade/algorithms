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
        def three_sum(target) -> None:
            def two_sum(target) -> None:
                aidxlookup = {}
                for bidx, firstnum in enumerate(arr):
                    if bidx > cidx:
                        if (target - firstnum in aidxlookup and aidxlookup[target - firstnum] not in (cidx, didx)):
                            res.append(sorted((target - firstnum, firstnum, c, d)))
                        aidxlookup[firstnum] = bidx
            
            for cidx, c in enumerate(arr):
                if cidx > didx:
                    two_sum(target - c)
        
        res = []
        for didx, d in enumerate(arr):
            three_sum(target - d)
        if not res:
            return []
        # print(res)
        res.sort()
        return res[0]

    return four_sum(s)

# arr = [1,2,3,4]
# s = 10
# print(find_array_quadruplet(arr, s))

# arr = [1,9,0,2,6,3,4]
# s = 10
# print(find_array_quadruplet(arr, s))

arr = [2, 7, 4, 0, 9, 5, 1, 3]
s = 20
res = [0,4,7,9]
myres = find_array_quadruplet(arr, s)
print(myres)
assert res == myres