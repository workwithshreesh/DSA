class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class queueUsingLL:
    def __init__(self):
        self.__head=None
        self.__tail=None
        self.__count=0

    def enqueue(self,element):
        newNode=Node(element)
        if self.__head is None:
            self.__head=newNode
            self.__tail=newNode
            self.__count+=1
        else:
            self.__tail.next=newNode
            self.__tail=self.__tail.next
            self.__count+=1

    def dequeue(self):
        if self.isEmpty():
            return -1
        data=self.__head.data
        self.__head=self.__head.next
        self.__count-=1
        return data

    def size(self):
        return self.__count

    def front(self):
        if self.isEmpty():
            return -1
        return self.__head.data

    def isEmpty(self):
        return self.__count==0
