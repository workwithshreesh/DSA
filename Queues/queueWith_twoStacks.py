class twoStacks:
    def __init__(self):
        self.stack1=[]
        self.stack2=[]

    def enqueue(self,element):
        while len(self.stack1)!=0:
            self.stack2.append(self.stack1.pop())

        self.stack1.append(element)

        while len(self.stack2)!=0:
            self.stack1.append(self.stack2.pop())

    def dequeue(self):
        if self.isEmpty():
            return -1

        return self.stack1.pop()

    def size(self):
        return len(self.stack1)

    def front(self):
        if len(self.stack1)==0:
            return -1
        return self.stack1[-1]

    def isEmpty(self):
        return self.size()==0


q=twoStacks()

q.enqueue(1)
q.enqueue(2)
q.enqueue(3)

while not q.isEmpty():
    print(q.dequeue())
