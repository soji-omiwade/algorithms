# will the queue have unbounded capacity
# will the support a timeout for put/get
# will the queue support blocking
# error handling for when the cap goes under (this shouldn't happend)
# should queue support join when all tasks complete?

class queue
instances:
    maxsize
    mutex = lock()
    condition variables based on the mutex
        notempty
        notfull
        alltasksdone
    unfinished tasks = 0
        
methods:
    task_done
        unfinished_tasks -= 1
        if unfinished_tasks == 0
            all_tasks_done.notify_all()
    join
        with alltasksdone:
            ...
    qsize
        with mutex
            return _qsize()
    put
        with notfull:
            while qsize >= maxsize
                notfull.wait()
            self._put(item)
            self.notempty.notify()
    def get(self, block=True, timeout=None):
        with notempty:
            if not block
                if self.qsize() == 0:
                    raise Exception("Empty!")
            #assumes timeout is None
            elif timeout is None:
                while qsize <= 0
                    # validation if it is < 0 goes here
                    self.notempty.wait()
            #now timeout is not None
            elif timeout < 0:
                raise ValueError()
            else:
                #wait timeout time at most
                #after that, quit waiting and raise Empty!
                #get item before end of wait? good exit while
                endtime = time() + timeout
                while self.qsize() == 0:
                    start = time()
                    notempty.wait(timeout)
                    timeout -= (time() - start)
            
            item = _get()
            self.notfull.notify()
            
def join(self):
