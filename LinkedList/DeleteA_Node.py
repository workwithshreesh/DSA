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


def deleteA(head,position):
    if (position<0 or position>length(head)):
        return head

    count=0
    prev=None
    curr=head
    while count<position:
        prev=curr
        curr=curr.next
        count+=1

    if prev is not None:
        prev.next = curr.next
    else:
        return


def takeInput():
    listInput=[int(ele) for ele in input('Enter a Num:').split()]
    head=None
    tail=None
    for currData in listInput:
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
deleteA(head,2)
printLL(head)