import threading, queue, time

q = queue.Queue()

def worker():
    print(f"enter worker {threading.get_ident()}")
    count = float("inf")
    while count > 0:
        item = q.get()
        print(f'{threading.get_ident()} working on {item}')
        time.sleep(2)
        print(f'\t\t{threading.get_ident()} finished {item}')
        count -= 1
        q.task_done()
    raise Exception("should never be here!")
        
# turn-on the work thread
threading.Thread(target=worker, daemon=True).start()
threading.Thread(target=worker, daemon=True).start()

#take a breath before starting
print("wait 5 seconds before giving workers work...")
time.sleep(5)

#send 30 task requests to the workers
for item in range(30):
    q.put(item)
print("all task requests sent\n", end='')

#block until all tasks are done
# q.join()
print("all work completed")