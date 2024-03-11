class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

def takeInput():
    inputList=[int(ele) for ele in input('Enter a num').split()]
    head=None
    for currData in inputList:
        if currData==-1:
            break
        newNode=Node(currData)
        if head is None:
            head=newNode
        else:
            curr=head
            while curr.next!=None:
                curr=curr.next
            curr.next=newNode
    return head

def printLL(head):
    while head is not None:
        print(f'{head.data}->',end='')
        head=head.next
    print(None)
    return

def Reverse(head):
    if head is None or head.next is None:
        return head
    smallHead=Reverse(head.next)
    tail=head.next
    tail.next=head
    head.next=None
    return smallHead

head=takeInput()
printLL(head)
head=Reverse(head)
printLL(head)