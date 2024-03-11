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



def length(head):
    count=0
    while head is not None:
        count+=1
        head=head.next
    return count




def Insert(head,i,data):

    if (i<0 or i>length(head)):
        return head

    count=0
    prev=None
    curr=head
    while count<i:
        prev=curr
        curr=curr.next
        count+=1
    newNode=Node(data)

    if prev is not None:
        prev.next=newNode
    else:
        head=newNode
    newNode.next=curr

    return head




def takeInput():

    InputList=[int(i) for i in input('Enter:').split()]

    head=None
    tail=None

    for currData in InputList:
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



head=takeInput()
printLL(head)
head=Insert(head,1,8)
printLL(head)