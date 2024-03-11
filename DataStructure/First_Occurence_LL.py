class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

def takeInput():
    inputList=[int(ele) for ele in input('Enter').split()]
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
            tail.next=newNode
            tail=newNode
    return head

def searchingOccurence(head,ele):
    curr=0
    while head!=None:
        if head.data==ele:
            print(curr)
            break
        curr+=1
        head=head.next
    return -1

def printLL(head):
    while head!=None:
        print(str(head.data)+'->',end='')
        head=head.next
    print(None)
    return

head=takeInput()
printLL(head)
searchingOccurence(head,3)

