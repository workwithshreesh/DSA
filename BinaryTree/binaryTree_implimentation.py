class BinaryTreeNode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None


bnode1=BinaryTreeNode(1)
bnode2=BinaryTreeNode(2)
bnode3=BinaryTreeNode(3)

# connection
bnode1.left=bnode2
bnode1.right=bnode3

