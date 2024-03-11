class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

def printLL(head):
    while head is not None:
        print(head.data,end=' ')
        head=head.next

def increement(head):
    temp=head
    while temp is not None:
        temp.data+=1
        temp=temp.next

node1=Node(10)
node2=Node(20)
node1.next=node2

increement(node1)
printLL(node1)