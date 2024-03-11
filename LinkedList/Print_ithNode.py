class Node:
    def __init__(self,data):
        self.data=data
        self.next=None



def printLL(head,i):
    if (i<0 or i>length(head)):
        return head

    count=0
    curr=head
    while count<i and curr!=None:
        curr=curr.next
        count+=1
    print(curr.data)
    return



def length(head):
    count=0
    while head is not None:
        count+=1
        head=head.next
    return count


def takInput():
    inputList=[int(ele) for ele in input('Enter a num:').split()]
    head=None
    tail=None
    for charDtat in inputList:
        if charDtat==-1:
            break

        newNode=Node(charDtat)

        if head is None:
            head=newNode
            tail=newNode
        else:
            tail.next=newNode
            tail=newNode
    return head


head=takInput()
printLL(head,2)


