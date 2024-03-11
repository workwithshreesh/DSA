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
        if head==None:
            head=newNode
        else:
            curr=head
            while curr.next!=None:
                curr=curr.next
            curr.next=newNode
    return head


def CountFunc(M,N,head):
    count1=1
    prev=head
    count2=1
    curr=head
    temp=head
    while temp!=None:
        while count1 <= M:
            count1 += 1
            prev = prev.next
            if prev.next == None:
                break


        while count2 <= (N + M):
            count2 += 1
            curr = curr.next
            if curr.next == None:
                break
        prev.next = curr
        curr.next=prev
        temp = temp.next
    return temp


def printLL(head):
    while head is not None:
        print(str(head.data)+'->',end='')
        head=head.next
    print(None)
    return

head=takeInput()
head=CountFunc(2,3,head)
printLL(head)
