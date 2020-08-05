# You are working with a team of meteorologists studying temperatures in a city. They have asked you to build a system that will track temperatures and provide metrics. 

# Your system should provide a function 'log(temperature)' that they will call once per second to record measured temperatures, as well as functions to query their data for useful metrics. Initially, they would like to be able to know:

# 1) the average of temperatures from the last 24 hours, and 
# 2) the maximum temperature from the last 24 hours

# As an example, if the meteorologists wanted to know the maximum temperature recorded for all time, your solution might look like this:

# Let max = NULL

# Log(temperature):
#   IF max IS NULL
#     Set max = temperature
#   ELSE IF temperature > max
#     Set max = temperature

# GetMaxAllTime:
#   Return max



#O(1)
from math import inf

def log(temperature):
    global daycount
    global daysum
    global alltime_max
    global alltime_count
    global alltime_sum
    
    #required for alltime_sum
    alltime_count += 1    
    
    #all time max needs to be calculated here for O(1) retrieval time
    if alltime_max is None:
        alltime_max = temperature
    alltime_max = max(temperature, alltime_max)

    #day sum and all time sum need to be calculated here for O(1) retrieval time
    if day_temps[daycount] != -inf:
        daysum -= day_temps[daycount]
    daysum += temperature
    alltime_sum += temperature
    
    #day_temps required for two reasons
    # 1) for getting the day sum, whehter in O(1) or O(n) time
    # 2) for getting day max period.
    day_temps[daycount] = temperature
    daycount = (daycount + 1) % daylength

def get_avg_day():
    return daysum / min(alltime_count, daylength)

def get_avg_all_time():
    return alltime_sum / alltime_count
    
#O(1)
def get_max_all_time():
    return alltime_max

#O(daylength)
#with a heapsort priority queue can be made O(log n)
def get_day_max():
    if day_temps[0] == -inf:
        return None
    return max(day_temps)

def get_day_max_fast():
    raise NotImplementedError
    
alltime_max = None
daysum = 0
lsum = 0
res = [(7,7), (7,7), (7,6), (7,5)]
daylength = 2
daycount = 0
day_temps = [-inf for i in range(daylength)]
exp_count = 4
for i in range(7,7-exp_count,-1):
    log(i)
    assert (get_max_all_time(), get_day_max()) == res[7-i]