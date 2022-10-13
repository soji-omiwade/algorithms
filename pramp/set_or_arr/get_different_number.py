'''
for 0 1 [1, 0, 1000, 205, 30]
0 1 [1, 0, 1000, 205, 30]
0 1 [0, 1, 1000, 205, 30]
0 1 [1, 1, 1000, 205, 30]
0 1 [1, 1, 1000, 205, 30]
0 1 [1, 1, 1000, 205, 30]
0 1 [1, 1, 1000, 205, 30]
0 1 [1, 1, 1000, 205, 30]
0 1 [1, 1, 1000, 205, 30]
0 1 [1, 1, 1000, 205, 30]
0 1 [1, 1, 1000, 205, 30]
'''
def get_different_number(arr):
  for idx in range(len(arr)):
    while idx != arr[idx] and arr[idx] < len(arr):
      arr[arr[idx]], arr[idx] = arr[idx], arr[arr[idx]]
  for idx, idxelem in enumerate(arr):
    if idx != idxelem:
      return idx
  return len(arr)

def enumerate__get_different_number(arr):
  count = 0
  for idx, idxelem in enumerate(arr):
    while idx != idxelem and (idxelem < len(arr)) and count < 10:
      count += 1
      temp = arr[idxelem] # idxelem = 42, idx = 0, arr[idxelem] = 58
      arr[idxelem] = idxelem # 
      idxelem = arr[idx] = temp
  for idx, idxelem in enumerate(arr):
    if idx != idxelem:
      return idx
  return len(arr)

arr = [0, 1, 2, 3]
print(get_different_number(arr)) #4

arr = [1, 0, 1000, 205, 30]
print(get_different_number(arr)) #2

