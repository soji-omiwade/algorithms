'''
12 62=> 1 26 2, 12 6 2,   1 2 6 2
 ^
 
card = 9
1 7 -> 1
1 9 -> 1

card = 26
1262 -> 
1 9 -> 1


1262
^

26 2

62

 ^
 
1262

2 62
^

62
^

2
^

gc + 1
'''
gc = 0 #global count

def decodeVariations(S):
  global gc
  
  def decode(numb):
    return 1 <= numb <= 26

  def count(string): #262    
    global gc
    if memo[i,j]:
      return memo[i,j]
    if not string: 
      gc += 1
      return
    n = len(string)
    for idx in range(n): # idx = 1 ==  
      if decode(int(string[:idx+1])):  #string[0:2]  =  26
        count(string[idx+1:n]) # 262 

  gc = 0
  count(S)
  return gc
S = '1262'
print(decodeVariations(S))


#https://pythontutor.com/render.html#mode=display
