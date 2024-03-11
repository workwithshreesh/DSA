class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

def takeInput():
    inputList=[int(ele) for ele in input('Enter:').split()]
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



def findmid(head):
    slow=head
    fast=head
    while fast.next!=None and fast.next.next!=None:
        slow=slow.next
        fast=fast.next.next

    return slow

def mergeSort(head1,head2):
    if not head1: #(Meaning) if head1==None
        return head2
    if not head2: #(Meaning) if head2==None
        return head1


    t1=head1
    t2=head2
    tail=None
    head=None
    if t1.data<=t2.data:
        head=t1
        tail=t1
        t1=t1.next
    else:
        head=t2
        tail=t2
        t2=t2.next

    while t1 and t2:
        if t1.data<=t2.data:
            tail.next=t1
            tail=t1
            t1=t1.next
        else:
            tail.next=t2
            tail=tail.next
            t2=t2.next

    if t1==None:
        tail.next=t2
    if t2==None:
        tail.next=t1

    return head


def Merging(head):
    if head==None:
        return head

    if  head.next==None:
        return head

    midNode=findmid(head)
    h2=midNode.next
    midNode.next=None
    part1=Merging(head)
    part2=Merging(h2)
    mergeList=mergeSort(part1,part2)

    return mergeList


def printLL(head):
    curr=head
    while curr is not None:
        print(str(curr.data)+'->',end='')
        curr=curr.next
    print(None)
    return

head=takeInput()
sort=Merging(head)
printLL(sort)