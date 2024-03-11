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



def insert(head,posit,data):
   if posit<0:
       return head

   if posit==0:
       newNode=Node(data)
       newNode.next=head
       return newNode

   if head is None:
       return None

   smallHead=insert(head.next,posit-1,data)
   head.next=smallHead
   return head


def takeInput():
    listInput=[int(ele) for ele in input('Enter a num:').split()]
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
insert(head,2,5)
printLL(head)