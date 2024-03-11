# input 1->2->3->4->5
# output 3

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
        if head==None:
            head=newNode
            tail=newNode
        else:
            tail.next=newNode
            tail=newNode

    return head

def midPoint(head):
    slow=head
    fast=head
    while(fast.next!=None and fast.next.next!=None):
        slow=slow.next
        fast=fast.next.next
    print(slow.data)
    return

def printLL(head):
    while head is not None:
        print(f'{head.data}->',end='')
        head=head.next
    print(None)
    return


head=takeInput()
printLL(head)
midPoint(head)