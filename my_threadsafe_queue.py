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
                    return None
            #assumes timeout is None
            while qsize <= 0
                # validatio if it is < 0 goes here
                self.notempty.wait()
            while 
            item = _get()
            notfull.notify()
def join(self):
