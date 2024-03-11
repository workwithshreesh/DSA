class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

def printLL(head):
    while head is not None:
        print(head.data,end=' ')
        head=head.next

node1=Node(10)
node2=Node(20)
node2.next=node1
printLL(node2)