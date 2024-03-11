class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

def takeInput():
    inputList=[int(ele) for ele in input('Enter').split()]
    head=None
    for currData in inputList:
        if currData==-1:
            break

        newNode=Node(currData)
        if not head:
            head=newNode
        else:
            curr=head
            while curr.next is not None:
                curr=curr.next
            curr.next=newNode
    return head

def printLL(head):
    while head is not None:
        print(str(head.data)+'->',end='')
        head=head.next
    print(None)
    return

def searchingOccurence(head,ele):
    curr=1
    if head is None or head.next is None:
        print(-1)
        return 0

    if head.data==ele:
        print(curr)
        return 0
    curr+=1
    searchingOccurence(head.next,ele)

head=takeInput()
ele=2
printLL(head)
searchingOccurence(head,ele)