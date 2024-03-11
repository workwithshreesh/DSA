class Node:
    def __init__(self,data):
        self.data=data
        self.next=None


def takeInput():
    listInput=[int(ele) for ele in input('Enter a num').split()]
    head=None
    for currData in listInput:
        if currData==-1:
            break
        newNode=Node(currData)
        if head is None:
            head=newNode
        else:
            curr=head
            while curr.next is not None:
                curr=curr.next
            if curr.data==newNode.data:
                curr.next=None
            else:
                curr.next=newNode
    return head



def printLL(head):
    while head is not None:
        print(str(head.data)+'->',end='')
        head=head.next
    print(None)
    return



head=takeInput()
printLL(head)