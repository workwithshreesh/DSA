class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

def printLL(head):
    i=0
    while head is not None:
        i+=1
        head=head.next
    print(i)
    return

def InputLinked():
    inputList=[int(ele) for ele in input('Enter a num:').split()]
    head=None
    for currData in inputList:
        if currData==-1:
            break
        newNode=Node(currData)
        if head is None:
            head=newNode
        else:
            curr=head
            while curr.next is not None:
                curr=curr.next
            curr.next=newNode

    return head

head=InputLinked()
printLL(head)