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
        if head==None:
            head=newNode
        else:
            curr=head
            while curr.next is not None:
                curr=curr.next
            curr.next=newNode
    return head

def mergeLL(head1,head2):

    if head1.data <= head2.data:
        finalHead = head1
        finalTail = head1
        head1 = head1.next
    else:
        finalHead = head2
        finalTail = head2
        head2 = head2.next

    while head1!=None and head2!=None:

        if head1.data<=head2.data:
            finalTail.next=head1
            finalTail=finalTail.next
            head1=head1.next

        else:
            finalTail.next=head2
            finalTail=finalTail.next
            head2=head2.next

    if head1==None:
        finalTail.next=head2

    if head2==None:
        finalTail.next=head1

    return finalHead


def printLL(head):
    while head is not None:
        print(str(head.data)+'->',end='')
        head=head.next
    print(None)
    return

head1=takeInput()
printLL(head1)
head2=takeInput()
printLL(head2)
finalHead=mergeLL(head1,head2)
printLL(finalHead)