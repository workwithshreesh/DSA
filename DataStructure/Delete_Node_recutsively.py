class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

def printLL(head):
    while head is not None:
        print(f'{head.data}->',end='')
        head=head.next
    print(None)
    return


def Delete(head,posit):
    if posit<0:
        return head
    curr=head
    if posit==0:
        head=head.next
        return head

    if head is None:
        return None

    smallDelete=Delete(head.next,posit-1)
    head.next=smallDelete
    return head



def takeInput():
    listInput=[int(ele) for ele in input('Enter a Num:').split()]
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
            curr.next=newNode

    return head

head=takeInput()
Delete(head,2)
printLL(head)