'''
10  0  6  15  8
   10  4  -5  2

curr_energy = ce
me = min energy to start

ce = 0
me = 0
for each height h after the first
  ce += - (h - last height)
  me = min(ce, me)
return -me
'''
def calc_drone_min_energy(route):
  ce = 0
  me = 0
  for hidx in range(1, len(route)):
    ce += route[hidx - 1][2] - route[hidx][2]
    me = min(ce, me)
  return -me
  
route = [ [0,   2, 0],
                  [3,   5,  0],
                  [9,  20,  5],
                  [10, 12, 115],
                  [10, 10,  80] ]
print(calc_drone_min_energy(route))

route = [ [0,   2, 10],
                  [3,   5,  0],
                  [9,  20,  6],
                  [10, 12, 15],
                  [10, 10,  8] ]
print(calc_drone_min_energy(route))

route = [ [0,   2, 10],
                  [3,   5,  10],
                  [9,  20,  10],
                  [10, 12, 10],
                  [10, 10,  10] ]
print(calc_drone_min_energy(route))




