def split_(ip):
  i = 0
  last = 0
  print("foo")
  while i < len(ip):
    if ip[i] == ".":
      yield ip[last:i]
      last = i + 1
    i += 1
  yield ip[last:]


'''
requirement:
. there must be a number between the dots (will do this later)
'''
def split_efficient(ip):
  num = None
  for i in range(len(ip)):
    if ip[i] == ".":
        yield num
        num = None
    elif num is not None and num > 255:
        yield None
    elif ord('0') <= ord(ip[i]) <= ord('9'):
        if num is None:
            num = 0
        num = (num * 10) + (ord(ip[i]) - ord('0'))
    else:
        yield None
  yield num
    
def validateIP(ip):
  tokens = split_efficient(ip)  
  count = 0
  for token in tokens:
    if token is None:
        return False
        
    if count == 4:
      return False
      
    if not 0 <= token <= 255:
        return False
    count += 1
  return True

# space complexity: O(len(ip)) --> O(1)
# time complexity: O(len(ip))
ip = '25.2.15568.0'    
print(validateIP(ip))
ip = '25.2.18.0'    
print(validateIP(ip))
ip = '25.2.oops.0'    
print(validateIP(ip))
ip = '25.2.18.0.52'    
print(validateIP(ip))
