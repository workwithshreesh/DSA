class Node:
    def __init__(self,data):
        self.data=data
        self.next=None


def takeInput():
    inputList=[int(ele) for ele in input('Enter:').split()]
    head=None
    for currData in inputList:
        if currData==-1:
            break

        newNode=Node(currData)
        if head is None:
            head=newNode
        else:
            curr=head
            while curr.next is not None:
                curr=curr.next
            curr.next=newNode
    return head


def searching(head,ele,curr=0):
    if head is None:
        return head
    searching(head.next,ele,curr+1)
    if head.data!=ele:
        print(curr)


def printLL(head):
    while head is not None:
        print(str(head.data)+'->',end='')
        head=head.next
    print(None)
    return

head=takeInput()
printLL(head)
ele=3
searching(head,3)