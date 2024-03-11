class Node:
    def __init__(self,val,next=None,prev=None):
        self.val=val
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
            newNode.prev=tail
            tail.next=newNode
            tail=newNode
    return head


def printLL(head):
    while head.next!=None:
        head=head.next

    while head!=None:
        print(str(head.val)+'->',end='')
        head=head.prev
    print(None)
    return

head=takeInput()
printLL(head)