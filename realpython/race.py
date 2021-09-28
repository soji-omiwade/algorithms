import concurrent.futures
import time
from collections import Counter
import sys
import threading

counter = 0
jobcount = int(sys.argv[1])
workloadsize = 100000

def increment_counter(fake_value):
    global counter
    workers[threading.get_ident()] += 1
    for _ in range(workloadsize):
        counter += 1


if __name__ == "__main__":
    res = []
    fake_data = [None] * jobcount

    #syncronous
    workers = Counter()
    start = time.time()
    counter = 0
    for x in fake_data:
        increment_counter(x)
    res.append(("synch", time.time() - start, counter, len(workers)))
    
    #concurrent
    workers = Counter()
    start = time.time()
    counter = 0
    with concurrent.futures.ThreadPoolExecutor(max_workers=jobcount) as executor:
        executor.map(increment_counter, fake_data)
    res.append(("threading", time.time() - start, counter, len(workers)))
    
    #print
    for approach, runtime, count_reached, workers_used  in res:
        print(f"{approach:10}: {runtime:.1f}, {count_reached}, {workers_used}")