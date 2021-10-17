from typing import int

class Solution:
    def solve(self, arr: List[int]) -> int:
        ...

sol = Solution()
a = [ [0, 30]       #---------------------
    , [5, 10]       #   -----
    , [15,20] ]     #          ------
print(sol.solve(a)) # 2

a = [ [1, 18]   #------------------
    , [18,23]   #                  ----
    , [15,29]   #              ----------
    , [4, 15]   #    ----------
    , [2, 11]   # ----------
    , [5, 13]   #     -------
    ]
print(sol.solve(a)) # 4

'''
heap method:
1. sort input by start time
1b. add first interval, which makes it the smallest_end_time_interval
2. then for all other intervals
    if intersects(interval, smallest_end_time_interval)
        add a room 
    else
        discard the interval with smallest end time
    regardless: add interval
illustrating min-heap method:
at each iteration, new element added to heap
    ------------------1        1, 18 -- initialize heap; room added
     ----------2               2, 11 -- new end time interval = (2,11); room added
        ----------3            4, 15 -- room added
         -------4              5, 13 -- room added
                  ----------4  15,29 -- discard (2,11), making end time = (5,13); hence, no room added
                      ----4    18,23 -- discard (5,13), making end time = (4,15); hence, no room added

----
    --
    ---
    -----
       ----

day
    7 - 4:30: 8 working 1 hour driving
    night: 
        femi in bed by 8:30pm
        cleanup to 9:30pm
        in bed by 10:30pm
        one time taking feyikemi: 1-2 hours
        up @ 6:30am
        out of the house @ 7am
        
getting a new car
    ask charlies dad about buying online
        - how did he get rid of old car
    
buying property
    look into redfin for houston real estate
'''
    
print(sol.solve(a)) # 
