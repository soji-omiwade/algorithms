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
def log(temperature):
    global count
    global maxtemp
    if maxtemp is None:
        maxtemp = temperature
    maxtemp = max(temperature, maxtemp)
    cropped_temps[count] = temperature
    count = (count + 1) % window_len
    
#O(1)
def get_max_all_time():
    return maxtemp

#O(window_len)
#with a heapsort priority queue can be made O(log n)
def get_day_max():
    if cropped_temps == []:
        return None
    return max(cropped_temps)

maxtemp = None
res = [(7,7), (7,7), (7,6), (7,5)]
window_len = 2
count = 0
cropped_temps = [float('-inf') for i in range(window_len)]
exp_count = 4
for i in range(7,7-exp_count,-1):
    log(i)
    assert (get_max_all_time(), get_day_max()) == res[7-i]