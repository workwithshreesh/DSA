class Node:
    def __init__(self,data):
        self.data=data
        self.next=None


def takeInput():
    inputList=[int(ele) for ele in input('Enter a num').split()]
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

def printLL(head):
    while head is not None:
        print(str(head.data)+'->',end='')
        head=head.next
    print(None)
    return


def isPalindrome(head):
    curr=head
    stack=[]

    if head is None:
        isPalin=True

    while curr is not None:
        stack.append(curr.data)
        curr=curr.next

    while head is not None:
        i=stack.pop()

        if head.data==i:
            isPalin=True
        else:
            isPalin=False
            break

        head=head.next

    print(isPalin)
    return


head=takeInput()
printLL(head)
isPalindrome(head)