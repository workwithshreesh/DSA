class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

def takeInput():
    inputList=[int(ele) for ele in input('Enter a Num').split()]
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

def Reverse(head):
    curr=head
    prev=None
    while curr is not None:
        next=curr.next
        curr.next= prev
        prev = curr
        curr = next
    head=prev
    return head

def printLL(head):
    while head is not None:
        print(str(head.data)+'->',end='')
        head=head.next
    print(None)
    return

head=takeInput()
printLL(head)
head=Reverse(head)
printLL(head)