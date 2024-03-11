class Node:
    def __init__(self,val,next=None):
        self.val=val
        self.next=next

def takeInput():
    inputList=[int(ele) for ele in input('Enter').split()]
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
            tail.next=newNode
            tail=newNode
    tail.next=head
    return head

def printCercular(head):
    temp=head.next
    while(temp!=head):
        print(str(temp.val)+'->',end='')
        temp=temp.next
    print(str(temp.val) + '->', end='')
    print(None)
    return

head=takeInput()
printCercular(head)