class Node:
    def __init__(self,data,prev=None,next=None):
        self.data=data
        self.prev=prev
        self.next=next

def takeInput():
    inputList=[int(ele) for ele in input('Enter:').split()]
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
            newNode.prev = tail
            tail.next=newNode
            tail=newNode

    return head

def printLL(head):
    print('Doubly Linked List')
    curr=None
    while head is not None:
        print(str(head.data)+'->',end='')
        if head.next is None:
            curr=head
        head=head.next

    while curr is not None:
        print(str(curr.data)+'->',end='')
        curr=curr.prev
    print(None)
    return


head=takeInput()
printLL(head)
