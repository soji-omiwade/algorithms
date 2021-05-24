from itertools import chain
'''
busiest day via zip
time 318 - 
'''
def busiest_day(data):
    maxpeople = people = 0
    for prev, curr in zip(chain([(None, 0, 0)], data), chain(data, [(None, 0, 0)])):
        if prev[0] != curr[0]:
            if people > maxpeople:
                maxtime = prev[0]
                maxpeople = people
        people += curr[1] * (1 if curr[2] else -1)
    return maxtime
    
data = [
(1, 5, 1)
]
assert busiest_day(data) == 1
data = [
(1, 5, 1), 
(1, 5, 1), 
(1, 5, 1),
(1, -15, 0), 
(2, 25, 1), 
(3, 10, 0), 
(3, 10, 1), 
]
assert busiest_day(data) == 2
data = [
(1, 5, 1), 
(1, 5, 1), 
(1, 5, 1),
(1, -15, 0), 
(2, 25, 1), 
(3, 10, 0), 
(3, 11, 1), 
]
assert busiest_day(data) == 3
