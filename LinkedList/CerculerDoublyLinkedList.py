class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None

def takeInput():
    inputList=[int(ele) for ele in input('Enter:').split()]
    head=None
    tail=None
    for currData in inputList:
        if currData==-1:
            break

        newNode=Node(currData)
        if not head:
            head=newNode
            tail=newNode
        else:
            newNode.prev=tail
            tail.next=newNode
            tail=newNode
    tail.next=head

    return head

# def printLL(head):
#     temp=head.next
#     while(temp!=head):
#         print(str(temp.data)+'->',end='')
#         temp=temp.next
#     print(str(temp.data))
#     return

def printLL(head):
    temp=head.next
    while temp!=head:
        temp=temp.next

    while temp!=head:
        print(str(temp.data)+'->',end='')
        temp=temp.prev
    return

head=takeInput()
printLL(head)