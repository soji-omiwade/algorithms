'''
Problem Statement
Your company has a big conference coming up and needs to book conference rooms in a convention center. To help the company save budget, we want to book as few conference rooms as possible given a list of meeting schedules that contains only the starting and ending time of each meeting. Write a program that helps figure out the minumum number of conference rooms needed.

Example:

[(2,7)] -> Output: 1
[(0,30),(5,10),(15,20) (21 22) (21 28) ] -> Explanation: Room1: (0,30) Room2: (5,10),(15,20) -> Output: 2
(0, 30), (0, 10), (5,15), (11, 20), (17, 25), (21,30)

examples
(0,30),   
(5,10), (15,20), (21 22)
(21 28)

(0, 30), (0, 10), (5,15), (11, 20), (17, 25), (21,30)
assumptions
approaches
1)
(0,30),   
(5,22),
(21 28)

2)
(0, 30), (0, 10), (5,15), (11, 20), (17, 25), (21,30)
0         1         2        3        4         5
0 30
count: 1

create a res array
for any new interval, look in res for a place where int has no intersection. this space defines a room!

tradeoffs
this appears to be the only way
'''
from typing import List, Tuple
def roomcount(times: List[Tuple[int, int]]) -> int:
    '''
        s1------e1
                s2-------e2
    '''
    def intersects(start1, end1, start2, end2):
        return min(end1, end2) > max(start1, start2) 
    
    def no_intersects(lis):
        for int_ in lis:
            if intersects(*int_, start, end): # return true if they touch?
                return False
        return True
        
    rooms = []
    for start, end in times:
        for lis in rooms:
            if no_intersects(lis):
                lis.append((start, end))
                break
        else:
            rooms.append([(start, end)])
    return len(rooms)
    
ints = [(2,7)] # -> Output: 1
print(roomcount(ints))
ints = [(0,30),(5,10),(15,20), (21, 22), (21, 28) ] #3
print(roomcount(ints))
ints = [(0,30),(5,10),(15,20),(21, 22), (22, 28) ] #2
print(roomcount(ints))