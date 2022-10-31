from itertools import chain
def calc_drone_min_energy(route):
  min_surplus = 0
  curr_surplus = 0
  for ridx in range(1, len(route)):
    curr_surplus += route[ridx - 1][2] - route[ridx][2]
    min_surplus = min(min_surplus, curr_surplus)
  return -min_surplus

route = [ [0,   2, 10],
                  [3,   5,  0],
                  [9,  20,  6],
                  [10, 12, 15],
                  [10, 10,  8] ]
print(calc_drone_min_energy(route))
