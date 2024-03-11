class BinaryTreeNode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None


def takeInput():
    rootData = int(input("Enter:"))

    if rootData==-1:
        return

    root = BinaryTreeNode(rootData)

    leftTree=takeInput()
    rightTree=takeInput()

    root.left = leftTree
    root.right = rightTree

    return root

def printDetail(root):
    if root==None:
        return None

    if root.left!=None:
        print("L",root.left.data,end='')

    if root.right!=None:
        print("R",root.right.data,end='')

    printDetail(root.left)
    printDetail(root.right)
    print(root.data)

root=takeInput()
printDetail(root)
