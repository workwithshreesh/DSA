from queues_implimantation import QueueUsingArray

callf=QueueUsingArray()

callf.enqueue(2)
callf.enqueue(3)
callf.enqueue(4)
callf.enqueue(5)

# while not callf.isEmpty():
#     print(callf.dequeue())

while (callf.isEmpty() is False):
    print(callf.front())
    callf.dequeue()

print(callf.dequeue())


from queueWithLL import queueUsingLL

qLL=queueUsingLL()

qLL.enqueue(1)
qLL.enqueue(2)
qLL.enqueue(3)
qLL.enqueue(4)

while (qLL.isEmpty() is False):
    print(qLL.front())
    qLL.dequeue()

print(qLL.dequeue())
