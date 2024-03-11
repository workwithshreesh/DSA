class QueueUsingArray:
    def __init__(self):
        self.__queue=[]
        self.__front=0
        self.__count=0

    def enqueue(self,element):
        self.__queue.append(element)
        self.__count+=1

    def dequeue(self):
        if self.isEmpty():
            print("Hey queue is empty!!!")
            return -1

        element= self.__queue[self.__front]
        self.__front+=1
        self.__count-=1
        return element

    def size(self):
        return self.__count

    def front(self):
        return self.__queue[self.__front]

    def isEmpty(self):
        return self.__count==0
