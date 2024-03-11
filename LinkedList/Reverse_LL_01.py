class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

def takeInput():
    inputList=[int(ele) for ele in input('Enter a num:').split()]
    head=None
    tail=None
    for currData in inputList:
        if currData==-1:
            break

        newNode=Node(currData)
        if head is None:
            head=newNode
            tail=newNode
        else:
            tail.next=newNode
            tail=newNode

    return head

def reverseLL(head):
    if head is None or head.next is None:
        return head,head

    smallHead,smallTail=reverseLL(head.next)
    smallTail.next=head
    head.next=None
    return smallHead,head

def printLL(head):
    while head is not None:
        print(str(head.data)+'->',end='')
        head=head.next
    print(None)
    return

head=takeInput()
printLL(head)
head,tail=reverseLL(head)
printLL(head)
