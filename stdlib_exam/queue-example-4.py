import queue

Empty = queue.Empty

class Stack(queue.Queue):
    "Thread-safe stack"
    
    def _put(self, item):
        # insert at the beginning of queue, not at the end
        self.queue.insert(0, item)

    # method aliases
    push = queue.Queue.put
    pop = queue.Queue.get
    pop_nowait = queue.Queue.get_nowait

#
# try it

stack = Stack(0)

# push items on stack
stack.push("first")
stack.push("second")
stack.push("third")

# print stack contents
try:
    while 1:
        print(stack.pop_nowait())
except Empty:
    pass

## third
## second
## first
