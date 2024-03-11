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


def Search(head,data):
    count=0
    while head is not None:
        if data==head.data:
            print(f'Index No:{count} and Data is {data}')
            count+=1
        count+=1
        head=head.next

    return


def takeInput():
    inputList=[int(ele) for ele in input('Enter Num:').split()]
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
printLL(head)
Search(head,2)