import queue
q= queue.Queue()
q.put(1)
q.put(2)
q.put(3)

while not q.empty():
    print(q.get())

q= queue.LifoQueue()
q.put(1)
q.put(2)
q.put(3)

while not q.empty():
    print(q.get())
