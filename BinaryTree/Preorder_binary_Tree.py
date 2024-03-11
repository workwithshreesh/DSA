class BinaryTreeNode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None


def takeInput():
    rootData=int(input("Enter:"))

    if rootData==-1:
        return

    root=BinaryTreeNode(rootData)

    leftTree=takeInput()
    rightTree=takeInput()

    root.left=leftTree
    root.right=rightTree

    return root

def printDetailed(root):
    if root==None:
        return None

    print(root.data,end='')
    if root.left!=None:
        print(root.left.data,end='')

    if root.right!=None:
        print(root.right.data,end='')


    printDetailed(root.left)
    printDetailed(root.right)

root=takeInput()
printDetailed(root)


