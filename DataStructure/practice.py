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

def ithPositon(head):
    takeInput=int(input("Enter number:"))
    count=0
    while head is not None:
        if head.data==takeInput:
            print(count)
        else:
            count+=1
        head=head.next
    return

def ithRecusion(head,count,Inpu):
    if head==None:
        return 0
    if head.data==Inpu:
        print(count)
    else:
        ithRecusion(head.next,count+1,Inpu)

def takeInput():
    inputList=[int(ele) for ele in input("Enter:").split()]
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

head=takeInput()
ithPositon(head)
ithRecusion(head,0,int(input("Enter Number:")))




