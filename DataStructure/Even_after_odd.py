class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

def takeInput():
    inputList=[int(ele) for ele in input('Enter').split()]
    head=None
    for currdata in inputList:
        if currdata==-1:
            break

        newNode=Node(currdata)
        if head is None:
            head=newNode
        else:
            curr=head
            while curr.next is not None:
                curr=curr.next
            curr.next=newNode
    return head

def oddeven(head):
    oddH=None
    oddT=None
    evenH=None
    evenT=None
    while head is not None:
        if (head.data%2==0):
            newNode=Node(head.data)

            if oddH==None:
                oddH=newNode
                oddT=newNode
                head=head.next
            else:
                oddT.next=newNode
                oddT=newNode
                head = head.next
        else:
            newNode = Node(head.data)

            if evenH == None:
                evenH = newNode
                evenT = newNode
                head = head.next
            else:
                evenT.next = newNode
                evenT = newNode
                head = head.next
    oddT.next=evenH
    return oddH

def printLL(head):
    while head!=None:
        print(str(head.data)+'->',end='')
        head=head.next
    print(None)
    return

head=takeInput()
print('Normal  ',end='')
printLL(head)
head=oddeven(head)
print('Even After Odd  ',end='')
printLL(head)
