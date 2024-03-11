class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

def printLL(head):
    while head is not None:
        print(str(head.data)+'->',end='')
        head=head.next
    print(None)
    return


def ReverseLL(head):
    if head is None or head.next is None:
        return head

    smallHead=ReverseLL(head.next)
    curr=smallHead
    while curr.next is not None:
        curr=curr.next
    curr.next=head
    head.next=None
    return smallHead


def takeInput():
    inputList=[int(ele) for ele in input('Enter data:').split()]
    head=None
    tail=None
    for currdata in inputList:
        if currdata==-1:
            break
        newNode=Node(currdata)
        if head is None:
            head=newNode
            tail=newNode
        else:
            tail.next=newNode
            tail=newNode

    return head


head=takeInput()
printLL(head)
head=ReverseLL(head)
printLL(head)

